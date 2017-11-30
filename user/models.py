from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Notice(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    cr_date = models.DateField()
class Noticeforowner(models.Model):
    subject = models.CharField(max_length=200)
    cr_date = models.DateField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    owner_id = models.CharField(max_length=45,blank=True)
    pname=models.CharField(max_length=45)
    longitude= models.DecimalField(max_digits=18, decimal_places=16,blank=False,null=True)
    latitude = models.DecimalField(max_digits=18,decimal_places=16,blank=False,null=True)
    contact_no= models.BigIntegerField(blank=True,null=True)
    address = models.CharField(max_length=70,blank=True)
    opening_time= models.TimeField(blank=True,null=True)
    closing_time= models.TimeField(blank=True,null=True)
    near_by_highway= models.NullBooleanField()
    website= models.CharField(max_length=45,blank=True,null=True)
    email_id= models.EmailField(blank=True,null=True)
    description = models.TextField(max_length = 100,null=True,blank=True)
    visits = models.BigIntegerField(null = True,blank=True)
    rating = models.BigIntegerField(null=True,blank=True)
    price_petrol= models.FloatField(null = True,blank=True)
    price_diesel = models.FloatField(null=True,blank=True)
    atm = models.NullBooleanField(null=True)
    toilets= models.NullBooleanField()
    air= models.NullBooleanField()
    first_aid = models.NullBooleanField()
    water = models.NullBooleanField()
    rest_room= models.NullBooleanField()
    card_accepted = models.NullBooleanField()
    last_updated= models.DateField(null=True)
    petrol = models.NullBooleanField()
    diesel = models.NullBooleanField()
    verified= models.NullBooleanField()
    city=models.CharField(null=True,blank=True,max_length=50),
    state=models.CharField(null= True,blank=True,max_length=50)
    district=models.CharField(null=True,blank=True,max_length=50)
   
    
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)