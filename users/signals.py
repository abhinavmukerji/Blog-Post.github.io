from django.db.models.signals import post_save   #gets fired when an object is saved/user is created
from django.contrib.auth.models import User  #this will be sender of the signal
from django.dispatch import receiver  #this will be receiver
from .models import Profile

#we are making this in order to make sure that Profile is created as soon as a user signs in our website

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()