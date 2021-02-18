from django.db.models.signals import post_save
from . import models as m
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        m.Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    m.Profile.save(user=instance)




