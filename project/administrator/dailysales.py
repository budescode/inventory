# import os
# import sys
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', '/home/budescode/inventory/project/project.settings')
import django
# django.setup()
from django.contrib import messages
from django.template.loader import get_template
from django.utils import timezone
from datetime import datetime
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
from models import Cart


def sendTotal():
    print('yeahhhhhhh')
# 	user = User.objects.get(username='budescode')
# 	subject = "Change Password"
# 	from_email = settings.EMAIL_HOST_USER
# 	# Now we get the list of emails in a list form.
# 	to_email = [user.email]
# 	#Opening a file in python, with closes the file when its done running
# 	detail2 = "https://www.1kshop.online/account/"+ str(test.user_id) + '/' + username
# 	with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
# 		sign_up_message = sign_up_email_txt_file.read()
# 	message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
# 	html_template = get_template("account/change_password_email.html").render({'detail2':detail2})
# 	message.attach_alternative(html_template, "text/html")
# 	message.send()
# 	date = datetime.now()
# 	cart = Cart.objects.filter(date=datetime.now())
# 	total_price = 0
# 	cart1 = Cart.objects.filter(date=datetime.now(), paid=True)
# 	total_cart = Cart.objects.filter(date=datetime.now(), paid=True).count()
# 	for i in cart1:
# 		total_price = total_price+i.price
#     # subject = "Daily Sales"
# 	subject, from_email, to = '1k shop customer email', gospeltruth18@gmail.com, 'gospeltruth18@gmail.com'
# 	text_content = 'This is an important message.'
# 	html_content = '<p>' + 'email : </br>' + 'gospeltruth18@gmail.com' +  '</p>' + '<p>' + 'name : </br>' + 'name' +  '</p>' + '<p>'+ 'Message : </br>'  + 'comment' + '</p> <br>'
# 	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
# 	msg.attach_alternative(html_content, "text/html")
# 	msg.send()
    # from_email = settings.EMAIL_HOST_USER
    # # Now we get the list of emails in a list form.
    # to_email = ['gospeltruth18@gmail.com']
    # #Opening a file in python, with closes the file when its done running
    # with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
    #     sign_up_message = sign_up_email_txt_file.read()
    # message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=to_email )
    # html_template = get_template("Administrator/dailyreport.html").render({'qs':cart1, 'total_cart':total_cart, 'total_price':total_price, 'date':date})
    # message.attach_alternative(html_template, "text/html")
    # message.send()