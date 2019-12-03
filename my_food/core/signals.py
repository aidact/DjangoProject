from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from core.models import Food, Wall


@receiver(post_delete, sender=Food)
def food_added(sender, instance, **kwargs):
    print(instance)
