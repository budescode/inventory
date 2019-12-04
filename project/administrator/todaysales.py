from administrator.models import Cart
import django
from django.contrib import messages
from django.template.loader import get_template
from django.utils import timezone
from datetime import datetime
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
print(Cart.objects.filter(user='budescode').count())
print('workingggg!!!!!')
# from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll

# class Command(BaseCommand):
#     help = 'Closes the specified poll for voting'

#     def add_arguments(self, parser):
#         parser.add_argument('poll_id', nargs='+', type=int)

#     def handle(self, *args, **options):
#         for poll_id in options['poll_id']:
#             try:
#                 poll = Poll.objects.get(pk=poll_id)
#             except Poll.DoesNotExist:
#                 raise CommandError('Poll "%s" does not exist' % poll_id)

#             poll.opened = False
#             poll.save()

#             self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))