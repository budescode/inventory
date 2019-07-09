from django.db import models

class CountryDetails(models.Model):
	postcode = models.CharField(max_length=100)
	suburb = models.CharField(max_length=100)
	state =models.CharField(max_length=100)
	dc = models.CharField(max_length=100)
	detail_type = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	ion = models.CharField(max_length=100)

	def __str__(self):
		return self.postcode


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
	category = models.CharField(max_length=20, choices = choices)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20)
	stock = models.IntegerField()

	def __str__(self):
		return self.category


class Cart(models.Model):
	category = models.TextField()
	description = models.TextField()
	qty = models.IntegerField(default=1)
	single_price = models.IntegerField(default=1)
	price = models.IntegerField()
	paid = models.BooleanField(default=False)
	name = models.TextField(default='')
	phonenumber = models.TextField(default='')
	date = models.DateField()

