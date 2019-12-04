from django import forms
from index.models import Index, IndexCategory, IndexSubCategory
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class IndexForm(forms.ModelForm):
	class Meta:
		exclude = ['category', 'subcategory', 'image1', 'image2', 'image3', 'image4', 'sex', 'size', 'price', 'rating']
		model = Index

class IndexCategoryForm(forms.ModelForm):
	class Meta:
		exclude = []
		model = IndexCategory
	def clean_name(self):
		name = self.cleaned_data.get('name')
		qs = IndexCategory.objects.filter(name=name)
		if qs.exists():
			raise forms.ValidationError("category already exists")
		return name
	# def clean(self):
	# 	cleaned_data = super().clean()
	# 	name = cleaned_data.get('name')
	# 	qs = IndexCategory.objects.filter(name=name)
	# 	if qs.exists():
	# 		raise forms.ValidationError("category already exists")
	# 	return name



class IndexSubCategoryForm(forms.ModelForm):
	class Meta:
		model = IndexSubCategory
		exclude = ['']
	def clean_name(self):
		name = self.cleaned_data.get('name')
		mycategory = self.cleaned_data.get('mycategory')
		qs = IndexSubCategory.objects.filter(name=name)
		if qs.exists():
			raise forms.ValidationError("category already exists")
		return name