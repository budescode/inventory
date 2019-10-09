from django.db import models

class Image(models.Model):
    image = models.FileField()
    def __str__(self):
        return str(self.id)
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
	category = models.ForeignKey(Category, on_delete = models.CASCADE, default=1, related_name='cartcategory')
	subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE, default=1, related_name='cartsubcategory')
	sex = models.TextField()
	qty = models.IntegerField(default=1)
	single_price = models.IntegerField(default=1)
	price = models.IntegerField()
	paid = models.BooleanField(default=False)
	date = models.DateField()
	size = models.CharField(max_length=10)
	product_id = models.IntegerField(default=1)
	paymentoption = models.CharField(max_length=20, null=True, blank=True, default='')


	def __str__(self):
	    return str(self.category)


