import datetime
from driverdocs.models import *
from django.core.mail import send_mail
from django.conf import settings
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'logistics.settings'

def B():
    subject = 'Hello world'
    message = f'Hi! Thank you for using application.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["example@gmail.com", ]
    send_mail( subject, message, email_from, recipient_list )
import os

from django.core.wsgi import get_wsgi_application