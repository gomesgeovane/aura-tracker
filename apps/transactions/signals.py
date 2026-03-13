from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction

@receiver(post_save, sender=Transaction)
def update_profile_aura(sender, instance, created, **kwargs):
    if created:
            profile = instance.recipient
            profile.aura += instance.aura
            profile.save()