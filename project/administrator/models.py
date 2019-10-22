from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.FileField()
    def __str__(self):
        return str(self.id)

class Category(models.Model):
    name = models.CharField(max_length=200)
    total_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    mycategory = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='mycategory')
    name = models.CharField(max_length=200)
    total_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class MyItems(models.Model):
	choices = (
		('Trouser', 'Trouser'),
		('Shorts', 'Shorts'),
		('T-Shirts', 'T-Shirts'),
		('Shoe', 'Shoe'),
		('Underwear', 'Underwear'),
		('Singlet', 'Singlet'),
		('Boxer', 'Boxer'),
		('Pant', 'Pant'),
		('Socks', 'Socks'),
		# ('Trouser', 'Trouser'),


		)
	category = models.ForeignKey(Category, on_delete = models.CASCADE, default=1, related_name='myitemscategory')
	subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE, default=1, related_name='subcategory')
	sex = models.TextField()
	size = models.CharField(max_length=10)
	price = models.DecimalField(decimal_places=2, max_digits=20)
	stock = models.IntegerField()

	def __str__(self):
		return str(self.category.name) + ' ' + str(self.subcategory.name) + ' ' + str(self.sex) + ' ' + str(self.size) + ' ' + str(self.stock)

class PettyCash(models.Model):
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, default=1, related_name='usercart')
	category = models.ForeignKey(Category, on_delete = models.CASCADE, default=1, related_name='cartcategory')
	subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE, default=1, related_name='cartsubcategory')
	sex = models.TextField()
	qty = models.IntegerField(default=1)
	single_price = models.IntegerField(default=1)
	price = models.IntegerField()
	paid = models.BooleanField(default=False)
	date = models.DateField()
	size = models.CharField(max_length=10)
	product_id = models.CharField(max_length=20, default='00')
	paymentoption = models.CharField(max_length=20, null=True, blank=True, default='')


	def __str__(self):
	    return str(self.category)


