from django.db import models
from django.contrib.auth.models import User
from index.models import Index
from order.models import Order


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Index, on_delete=models.CASCADE, default=1, related_name='cart_index')
	style= models.CharField(max_length=60, default='')
	size = models.CharField(max_length=10)
	sex = models.CharField(max_length=10)
	quantity = models.IntegerField()
	paid=models.BooleanField(default=False)
	unit_price = models.PositiveIntegerField(default=1000)
	total_price = models.PositiveIntegerField(default=1000)
	order_key = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='order_name')
	ordered = models.BooleanField(default=False)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)
	def __str__(self):
		return self.user.username

