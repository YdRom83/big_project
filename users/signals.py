from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

def profile_updated(sender, instance, created, **kwargs):
    print("Profile Saved!")
    print("Sender:", sender)
    print("Instance:", instance)
    print("Created:", created)

def delete_user(sender, instance,  **kwargs):
    print("Deleting user...")


post_save.connect(profile_updated, sender=Profile)    

post_delete.connect(delete_user, sender=Profile)