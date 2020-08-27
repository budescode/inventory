from django.core.management.base import BaseCommand
from django.utils import timezone
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from administrator.models import Cart, CartItems
from django.contrib.auth.models import User


class Command(BaseCommand):
	help = 'Daily report '
	def handle(self, *args, **kwargs):
		cashier = User.objects.get(username='cashier')
		cashier02 = User.objects.get(username='cashier02')
		qs = CartItems.objects.filter(date=timezone.now(), user=cashier)
		carttotal = 0
		cartprice = 0
		for i in qs:
			carttotal = carttotal + i.quantity
			cartprice = cartprice + (i.quantity * 1000)
		subject = "Daily Report"
		from_email = settings.EMAIL_HOST_USER
		# Now we get the list of emails in a list form. infoyeghscompany
		to_email = ['infoyeghscompany@gmail.com']
    	#Opening a file in python, with closes the file when its done running
		with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
			sign_up_message = sign_up_email_txt_file.read()
		message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
		html_template = get_template("account/dailyreport.html").render({'qs':qs, 'carttotal':carttotal, 'cartprice':cartprice})
		message.attach_alternative(html_template, "text/html")
		message.send()

		qs = CartItems.objects.filter(date=timezone.now(), user=cashier02)
		carttotal = 0
		cartprice = 0
		for i in qs:
			carttotal = carttotal + i.quantity
			cartprice = cartprice + (i.quantity * 1000)
		subject = "Daily Report"
		from_email = settings.EMAIL_HOST_USER
		# Now we get the list of emails in a list form.
		to_email = ['infoyeghscompany@gmail.com']
		#Opening a file in python, with closes the file when its done running
		with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
			sign_up_message = sign_up_email_txt_file.read()
		message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
		html_template = get_template("account/dailyreport.html").render({'qs':qs, 'carttotal':carttotal, 'cartprice':cartprice})
		message.attach_alternative(html_template, "text/html")
		message.send()