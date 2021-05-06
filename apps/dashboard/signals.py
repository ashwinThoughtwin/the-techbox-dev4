from django.db.models.signals import post_save,post_init,post_delete
from django.db.models.signals import pre_save,pre_init,pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Tool
from django.core.mail import send_mail
from django.conf import settings
from .tasks import toolcreate_mail


@receiver(post_save, sender=Tool)
def create_tool(sender, instance, created, **kwargs):
    if created:
        # name = instance.name
        # subject = f'{name} is  created '
        # message = f'Hi {name} is created successfully'
        # recipient_list = ['ishwarmandloi25@gmail.com', ]
        # toolcreate_mail.delay(subject,message,recipient_list)

        print("-----------------------------------")
        print("post save signal...")
        print("New Record")
        print("Sender:",sender)
        print("Instance:",instance)
        print("created:",created)
        print(f'kwargs: {kwargs}')

    else:
    	print("-----------------------------------")
    	print("post save signal...")
    	print("Update")
    	print("Sender:",sender)
    	print("Instance:",instance)
    	print("created:",created)
    	print(f'kwargs: {kwargs}')
