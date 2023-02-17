from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile


# user profile should be created for every new user 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): 
    # if a user is created, a signal should be sent to create a Profile where the user is the instance 
    if created: 
            Profile.objects.create(user=instance)
            
# user profile should be created for every new user 
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs): 
    # if a user is created, a signal should be sent to create a Profile where the user is the instance 
    instance.profile.save() 
            

            
        