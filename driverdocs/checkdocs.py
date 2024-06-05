import datetime
from driverdocs.models import *
from django.core.mail import send_mail
from django.conf import settings
def A():
    now1 = datetime.datetime.now().date()
    end_day = now1 + datetime.timedelta(days=30)
    days = Documents.objects.filter(doc_expire__lte=end_day)

    for day in days:
        print(day.doc_expire)

subject = 'Hello world'
message = f'Hi! Thank you for using application.'
email_from = settings.EMAIL_HOST_USER
recipient_list = ["example@gmail.com", ]
send_mail( subject, message, email_from, recipient_list )
