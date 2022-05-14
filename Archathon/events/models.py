from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	Bio =models.CharField(max_length=500, null=True)
	Organization=models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.name



class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class event(models.Model):
	CATEGORY = (
			('dance', 'Dance'),
			('music', 'Music'),('arts','Arts'),('crafts','Crafts'),('learn','Learn'),
			) 

	Event_Title = models.CharField(max_length=200,unique=True, null=True)
	
	
	Event_Banner=models.ImageField()
	short_desc = models.TextField(null=True)
	description = models.TextField(null=True)
	Phone_NO = models.IntegerField(null=True,)

	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# tags = models.ManyToManyField(Tag)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	count=models.IntegerField(null=True,)
	count2=models.IntegerField(null=True,)
	cancel_event=models.BooleanField(null=True, default=False)
	

	def __str__(self):
		return self.Event_Title







class register(models.Model):
	STATUS = (
			
			('YES', 'YES'),
			('MAYBE','MAYBE'),
			('NO', 'NO'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL,)
	event_name = models.ForeignKey(event, null=True, on_delete= models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	Location=models.CharField(max_length=200, null=True)
	Proposed_Date= models.DateField(null=True)
	Proposed_Time=models.TimeField(null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default='NO')
	count=models.IntegerField(null=True,)
	

	def __str__(self):
		return self.name

class info(models.Model):
   

    title= models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images/info')
    Short_Desc= models.TextField()
    long_Desc= models.TextField()
    
class all_photos(models.Model):
    photo_name=models.CharField(max_length=100, )
    photo=models.ImageField(upload_to='images/events')
    photo_Desc= models.TextField(blank=True)

    def __str__(self):
        return self.photo_name
	
