from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#date and time
# from datetime import date, time
from datetime import datetime
#from matplotlib.style import context
#from matplotlib.style import context

from sqlalchemy import false
today=datetime.now()

date=today.strftime("%Y-%m-%d")
date2=today.strftime("%B %d, %Y")




# Create your views here.
from .models import *
from .forms import *
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			#Added username after video because of error returning customer name if not added
			Customer.objects.create(
				user=user,
				name=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)
def gallery(request):
	photos=all_photos.objects.all
	context={'photos':photos}
	return render(request, 'Gallery/index.html', context)
def logoutUser(request):
	logout(request)
	return redirect('login')

def participants(request):
	
	return render(request, 'accounts/participants.html',)
def learn(request):
	
	return render(request, 'Learn/index.html',)
def nft(request):
	
	return render(request, 'nft/index.html',)
def upcoming(request):
	
	return render(request, 'upcoming/index.html',)
def admin(request):
	event_user = request.user.customer.event_set.all().order_by('-id')
	registered_user=request.user.customer.register_set.all().order_by('-id')
	register_event=register.objects.all()
	
		
		

	na=[]
	for event in register_event:
		nam=event.event_name
		na.append(nam)

	all_event=[]
	

	for event in event_user:
	
		c=0
		for i in all_event:
			
			if event.Event_Title==i:
				
				c+=1
		event.count=c
	


						
			


	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()
	# orders = request.user.customer.order_set.all()

	Event_created = event_user.count()
	Event_registered = registered_user.count()
	
	# today=date.today()
	# d= today.strftime("%m/%d/%Y")
	# print('date',d)
	

	

		            
	
	# delivered = orders.filter(status='Delivered').count()
	# pending = orders.filter(status='Pending').count()

	

	context = {'total_registered_events':Event_registered, 'total_event_created':Event_created,
	'form':form,'created_events':event_user,'registered_events':registered_user,'customer':customer,'list':list,}
	return render(request, 'accounts/admin.html', context)
def info1(request):
	return render(request, 'Archathon/info.html',)
def home(request):
	
	val=1
	admin=0
	l=request.user.groups.values_list('name',flat=True)
	for i in l:
		if i == 'super':
			
			admin=1
		else:
			admin=0
	
	infos=info.objects
	events = event.objects.all().order_by('-id')
	if request.user.is_authenticated:
		registered_user=request.user.customer.register_set.all().order_by('-id')
		count2=registered_user.count()
		count2=count2-3
		count=events.count()
		count=count-3
		customer = request.user.customer
		# event_user = request.user.customer.event_set.all()
		events1 = event.objects.all()

		


		context={'events':events,'customer':customer,'count':count,'registered_event':registered_user,'register_count':count2,'list':list,'info':infos,'admin':admin,'val':val,}

		return render(request, 'Archathon/index.html', context)
	else:
		count=events.count()
		count=count-3
		
		# event_user = request.user.customer.event_set.all()
		events1 = event.objects.all()

		
		return render(request, 'Archathon/index.html', {'events':events,'count':count,'info':infos,'admin':admin,'val':val,})

def All_Upcoming_Event(request):
	events = event.objects.all().order_by('-id')
	events1 = events

	
	context={'events':events,}

	return render(request, 'accounts/all_upcoming_event.html', context)
@login_required(login_url='login')
def All_registered_Event(request):
	events1 = event.objects.all()

	list=[]
	for even in events1:
		
		if str(even.Event_Date) < str(date):
			a=even.Event_Title
			list.append(a)
	registered_user=request.user.customer.register_set.all().order_by('-id')
	context={'events':registered_user,'list':list}

	return render(request, 'accounts/all_registered_event.html', context)


def index(request):
	events = event.objects.all().order_by('-id')
	context={'events':events,}

	return render(request, 'accounts/index.html', context)

@login_required(login_url='login')

def userPage(request):
	event_user = request.user.customer.event_set.all().order_by('-id')
	registered_user=request.user.customer.register_set.all().order_by('-id')
	register_event=register.objects.all()
	
	val=1
	l=request.user.groups.values_list('name',flat=True)
	for i in l:
		if i == 'super':
			
			admin=1
		else:
			admin=0

	
			
	
			
			


	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()
	# orders = request.user.customer.order_set.all()

	Event_created = event_user.count()
	Event_registered = registered_user.count()
	
	# today=date.today()
	# d= today.strftime("%m/%d/%Y")
	# print('date',d)
	

	

		            
	
	# delivered = orders.filter(status='Delivered').count()
	# pending = orders.filter(status='Pending').count()

	

	context = {'total_registered_events':Event_registered, 'total_event_created':Event_created,
	'form':form,'created_events':event_user,'registered_events':registered_user,'customer':customer,'admin':admin,'val':val,}
	return render(request, 'accounts/user.html', context)

@login_required(login_url='login')

def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')

def events(request, pk):

	EventFormSet = inlineformset_factory(Customer, event, fields=('Event_Title', 'short_desc', 'Phone_NO' , 'Event_Banner', 'description',),extra=1,widgets= {
			'Event_Date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
			'Event_Time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
		})
	customer = Customer.objects.get(id=pk)
	formset = EventFormSet(queryset=event.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = EventForm(request.POST)
		formset = EventFormSet(request.POST,request.FILES, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('user-page')


	context = {'form':formset}

	return render(request, 'accounts/Create_Event.html', context)


def Event_details(request,pk):
	
	all_event=event.objects.all()
	all_register=register.objects.all()
	events = event.objects.get(id=pk)
	count=0
	
	
	

	



	context={'event':events,'count':count,}

	return render(request, 'Archathon/Event_details.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')

def RegisterEvent(request, pk):
	user=request.user.customer
	event_user = request.user.customer.event_set.all()
	print(event_user)
	registered_user=request.user.customer.register_set.all()
	print(registered_user)
	register_event=register.objects.all()
	print(register_event)

	n=[]
	for even in registered_user:
		nam=even.event_name
		n.append(nam)

	all_even=[]
	
	



	na=[]
	for even in register_event:
		nam=even.event_name
		na.append(nam)

	

	Event=event.objects.get(id=pk)
	p_name=Event.Event_Title
	
	reg=0
	for even in all_even:
	
		reg=0
		
			
		if even==p_name:
			
			reg=1
			break
	
	
	
	
	# EventFormSet = inlineformset_factory(Customer, register, fields=('name','Organization','phone','email','event_name'),extra=1,)
	customer = request.user.customer
	# formset = EventFormSet(instance=customer)
	formset = EventRegisterForm(initial={'event_name':Event,'customer':customer})
	
	
	if request.method == 'POST':
		print("post")
		#print('Printing POST:', request.POST)
		#form = EventForm(request.POST)
		formset = EventRegisterForm(request.POST,)
		if formset.is_valid():
			formset.save()
			return redirect('user-page')
		else:
			print("failed ffff")

	context = {'form':formset,'event':Event,'registered':reg}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')

def updateEvent(request, pk):
	event_user=request.user.customer.event_set.all()
	Event = event.objects.get(id=pk)
	name=Event.Event_Title
	na=[]
	for even in event_user:
		nam=even.Event_Title
		na.append(nam)
	

	form = EventForm(instance=Event)

	if request.method == 'POST':

		form = EventForm(request.POST, instance=Event)
		if form.is_valid():
			form.save()
			return redirect('user-page')

	context = {'form':form}
	return render(request, 'accounts/update.html', context)

	return HttpResponse('<h1>You are not authorized to be here <h2>')

@login_required(login_url='login')
def deleteEvent(request, pk):
	event_user=request.user.customer.event_set.all()
	Event = event.objects.get(id=pk)

	name=Event.Event_Title
	na=[]
	for even in event_user:
		nam=even.Event_Title
		na.append(nam)

	if name in na:
		form = DeletForm(instance=Event)
		
		if request.method == 'POST':

			form = DeletForm(request.POST, instance=Event)
			if form.is_valid():
				form.save()
				return redirect('user-page')

		context = {'form':form,'event':Event}
		return render(request, 'accounts/delete.html', context)
	else:
		return HttpResponse('<h1>You are not authorized to be here <h2>')
@login_required(login_url='login')
def updateRegister(request, pk):
	registered_user=request.user.customer
	print(registered_user)
	print(pk)
	Event = register.objects.get(id=pk)
	print(Event)
	

	# if name in na:
	form = UpdateRegisterForm(instance=registered_user)
		
	if request.method == 'POST':

		form = UpdateRegisterForm(request.POST, instance=registered_user)
		if form.is_valid():
			form.save()
			return redirect('user-page')

	context = {'form':form}
	return render(request, 'accounts/update.html', context)
	# else:
	# 	return HttpResponse('<h1>You are not authorized to be here <h2>')

def confirm(request, pk):
	registered_user=request.user.customer.register_set.all()
	reg_event= registered_user.get(id=pk)
	reg=reg_event.event_name.Event_Title
	
	form = ConfirmForm(instance=reg_event)
	
	if request.method == 'POST':

		form = ConfirmForm(request.POST, instance=reg_event)
		if form.is_valid():
			form.save()
			return redirect('user-page')

	context = {'form':form,'event':reg}
	return render(request, 'accounts/confirm.html', context)
	



# @login_required(login_url='login')

# def deleteEvent(request, pk):
# 	events = event.objects.get(id=pk)
# 	if request.method == "POST":
# 		events.delete()
# 		return redirect('home')

# 	context = {'item':events}
# 	return render(request, 'accounts/delete.html', context)