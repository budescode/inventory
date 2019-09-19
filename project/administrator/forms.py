from django.contrib.auth.models import User
from django import forms
from .models import PettyCash

class PettyCashForm(forms.ModelForm):
	class Meta:
		model = PettyCash
		exclude = ['']
