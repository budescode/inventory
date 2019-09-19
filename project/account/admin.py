from django.contrib import admin

from .models import Profile, ChangePasswordCode
admin.site.register(Profile)
admin.site.register(ChangePasswordCode)
