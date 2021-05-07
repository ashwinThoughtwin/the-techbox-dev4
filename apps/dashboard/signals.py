from django.db.models.signals import post_save,post_init,post_delete
from django.db.models.signals import pre_save,pre_init,pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Tool
from techbox.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Tool)
def create_tool(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        model_number = instance.model_number
        subject = 'NAME: {0}, DESCRIPTION: {1},'.format(name, model_number)
        message = 'A New Tech Tool is Created!\n'
        message += 'NAME: ' + name + '\n' + 'DESCRIPTION: ' \
                   + model_number + '\n'
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            ['ishwar.thoughtwin@gmail.com', ],
            fail_silently=False,
        )
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
