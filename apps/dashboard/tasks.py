from __future__ import absolute_import, unicode_literals
from datetime import datetime
from celery import shared_task
from celery.app.base import app_has_custom
from django.http.response import HttpResponse 
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
from django.apps import apps
from dashboard.models import BorrowTool



@shared_task()
def toolcreate_mail(subject, message, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)
    return "create Tool successfully "




def mail(mail_list,tool,expire,name):
    subject = 'welcome '
    message = f'Hi {name}, You have got {tool}. for {expire}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = mail_list
    send_mail( subject, message, email_from, recipient_list )



@shared_task
def send_mail():
    queryset=BorrowTool.objects.filter(expire_on__lte=datetime.now().date())
    mail_list=[]
    for employee in queryset:
        email=employee.employee.email
        name=employee.employee.name
        tool =employee.tool
        expire=employee.expire_on
        mail_list.append(email)
        mail(mail_list,tool,expire,name)
        


