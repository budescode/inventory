from django.db import models
from django.contrib.auth.models import User


class IndexSize(models.Model):
	size = models.CharField(max_length=10)

	def __str__(self):
		return self.size

class IndexCategory(models.Model):
    name = models.CharField(max_length=200)
    total_count = models.IntegerField(default=0)
    image = models.FileField(default='')
    def __str__(self):
        return self.name

class IndexSubCategory(models.Model):
    mycategory = models.ForeignKey(IndexCategory, on_delete=models.CASCADE, default=1, related_name='indexcategory')
    name = models.CharField(max_length=200)
    total_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Index(models.Model):
	sex_choices = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Unisex', 'Unisex'),
		('Kids', 'Kids'),

		)
	size_choices = (
		('S', 'S'),
		('M', 'M'),
		('L', 'L'),
		('XL', 'XL'),
		('2XL', '2XL'),
		('3XL', '3XL'),
		('4XL', '4XL'),



		)
	category = models.ForeignKey(IndexCategory, on_delete = models.CASCADE, default=1, related_name='index_category')
	subcategory = models.ForeignKey(IndexSubCategory, on_delete = models.CASCADE, default=1, related_name='index_subcategory')
	name = models.CharField(max_length=90, null=True, blank=True)
	color = models.CharField(max_length=25)
	image = models.ImageField(upload_to = 'index_images')
	available = models.BooleanField(default=True)
	image1 = models.ImageField(upload_to = 'index_images', null=True, blank=True)
	image2 = models.ImageField(upload_to = 'index_images', null=True, blank=True)
	image3 = models.ImageField(upload_to = 'index_images', null=True, blank=True)
	image4 = models.ImageField(upload_to = 'index_images', null=True, blank=True)
	sex = models.CharField(max_length=10, choices=sex_choices)
	size = models.CharField(max_length=10, choices=size_choices)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	stock = models.IntegerField()
	rating = models.PositiveIntegerField(null=True, blank=True, default=0)

	def __str__(self):
		return self.category.name + ' ' + self.subcategory.name

class Favourite(models.Model):
    product_id = models.ForeignKey(Index, on_delete=models.CASCADE, default=1, related_name='favourite_category')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
