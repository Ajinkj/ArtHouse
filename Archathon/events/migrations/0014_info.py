# Generated by Django 3.0.3 on 2022-05-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20210523_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images/info')),
                ('Short_Desc', models.TextField()),
                ('long_Desc', models.TextField()),
            ],
        ),
    ]
