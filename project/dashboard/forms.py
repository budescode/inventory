from django import forms
from index.models import Index, IndexCategory, IndexSubCategory

class IndexForm(forms.ModelForm):
	class Meta:
		exclude = ['category', 'subcategory', 'image1', 'image2', 'image3', 'image4', 'sex', 'size', 'price', 'rating']
		model = Index

class IndexCategoryForm(forms.ModelForm):
	class Meta:
		exclude = []
		model = IndexCategory
	def clean(self):
		cleaned_data = super().clean()
		name = cleaned_data.get('name')
		unisex = cleaned_data.get('unisex')
		print(name, unisex)
		qs = IndexCategory.objects.filter(name=name, unisex=unisex)
		if qs.exists():
			raise forms.ValidationError("Records already exists")
		return str(name)


PRODUCT_QUANTITY_CHOICES = [('Men',"Men"), ("Women", "Women"), ("Boys", "Boys"), ("Girls", "Girls")]

class IndexSubCategoryForm(forms.ModelForm):
	unisex = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	class Meta:
		model = IndexSubCategory
		exclude = ['']
	def clean_name(self):
		name = self.cleaned_data.get('name')
		mycategory = self.cleaned_data.get('mycategory')
		return name