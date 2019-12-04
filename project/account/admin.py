from django.contrib import admin

from .models import Profile, ChangePasswordCode, RegistrationConfirm
admin.site.register(Profile)
admin.site.register(ChangePasswordCode)
admin.site.register(RegistrationConfirm)
