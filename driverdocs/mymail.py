from django.core.wsgi import get_wsgi_application
import sys
print(sys.path)
sys.path.append('E:\\sadiplomo')

from django.conf import settings
import django

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import get_template


import sadiplomo.wsgi
from django.shortcuts import get_object_or_404
import datetime
django.setup()
from users.models import User


from driverdocs.models import *
from cardocs.models import *


now1 = datetime.datetime.now().date()
end_day = now1 + datetime.timedelta(days=90)
days = Documents.objects.filter(doc_expire__lte=end_day)


now2 = datetime.datetime.now().date()
end_day2 = now2 + datetime.timedelta(days=30)
days2 = CarDocuments.objects.filter(car_doc_expire__lte=end_day)


html_temp = "driverdocs/docs_data_send.html"
context_data = {'doc':days, 'doccars': days2}

email_html_temp = get_template(html_temp).render(context_data)
recipient_list = ["example@gmail.com"]


subject1 = 'შეტყობინება'
email_from = "example@gmail.com"
"""
email_msg = EmailMessage(


	subject1,
	email_html_temp,
    email_from,
	recipient_list,
	["example@gmail.com"]
	)

email_msg.content_type = "html"
email_msg.send(fail_silently=False)
"""


from django.core.mail import EmailMultiAlternatives


subject, from_email, to = subject1,email_from, recipient_list
text_content = ''
html_content = email_html_temp
msg = EmailMultiAlternatives(subject, text_content, from_email, to)
msg.attach_alternative(html_content, "text/html")
msg.send()

