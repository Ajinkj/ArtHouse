# Generated by Django 3.0.3 on 2021-05-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20210523_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Meet_link',
            field=models.CharField(blank=True, default='none', max_length=2000),
        ),
    ]