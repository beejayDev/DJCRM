from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    cellphone_field = models.CharField(max_length = 15)

class Lead(models.Model):
    #SOURCE_CHOICES = (
            #('Youtube', 'YouTube'),
            #('Google', 'Google'),
            #('Newsletter', 'Newsletter')
            #)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField(default = 0)
    agent = models.ForeignKey(to="Agent", on_delete = models.CASCADE)
    #phoned = models.BooleanField(default = False)
    #source = models.CharField(choices=SOURCE_CHOICES, max_length = 100)
    #profile_pics = models.ImageField(blank = True, null = True)
    #special_files = models.FileField(blank = True, null = True)

class Agent(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    #leads = models.ForeignKey(Lead, on_delete = models.CASCADE)
    user = models.OneToOneField(to=User,on_delete =  models.CASCADE)
