from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid



class PasswordResetEmail(models.Model):
	email = models.EmailField()
class ChangePasswordCode(models.Model):
	username = models.CharField(max_length=50)
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
class ChangePassword(models.Model):
	new_password = models.CharField(max_length=50, blank = False, null = False)
	confirm_new_password = models.CharField(max_length=50, blank = False, null = False)


class Profile(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField()
	photo=models.FileField()


class UserRegister(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=13, help_text='Starts with +910')
	email = models.EmailField()
	password = models.CharField(max_length=100)


# def create_profile(sender, **kwargs):
# 	user = kwargs["instance"]
# 	if kwargs["created"]:
# 		user_profile = Profile(user=user)
# 		user_profile.save()
# post_save.connect(create_profile, sender=User)

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#        profile, created = Profile.objects.get_or_create(user=instance)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()