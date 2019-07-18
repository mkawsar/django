from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Role


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_save(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_role(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_save(sender, instance, **kwargs):
    instance.role.save()
