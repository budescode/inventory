from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
	payment_choices = (
		('Online', 'Online'),
		('Delivery', 'Delivery'),
		('Transfer', 'Transfer'),

		)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	address = models.TextField()
	phone_number = models.TextField()
	email = models.EmailField()
	order_id = models.TextField()
	delivered = models.BooleanField(default=False)
	paid=models.BooleanField(default=False)
	paymentoption = models.CharField(max_length=20, null=True, blank=True, default='', choices=payment_choices)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)
	def __str__(self):
		return self.user.username