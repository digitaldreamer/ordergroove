from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib.sites.models import Site


@receiver(post_save, sender=User)
def new_user(sender, **kwargs):
    site = Site.objects.get_current()

    if kwargs['created']:
        context = {
            'site': Site.objects.get_current(),
            'user': kwargs['instance'],
        }

        subject = 'Welcome to %s' % site.name
        message = render_to_string('registration/emails/registered.txt', context)
        to_email = kwargs['instance'].email
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail(subject, message, to_email, [from_email], fail_silently=False)
