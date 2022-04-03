from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserInformation


@receiver(post_save, sender=User)
def created_user(sender, instance, created, **kwargs):
    if created:
        UserInformation.objects.create(user=instance)
        print("created")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userinformation
    instance.userinformation.save()
    print("updated")
