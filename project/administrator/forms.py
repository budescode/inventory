from django.contrib.auth.models import User
from django import forms
from .models import PettyCash, SubCategory

class PettyCashForm(forms.ModelForm):
	class Meta:
		model = PettyCash
		exclude = ['']
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        exclude = ['']