import datetime

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from core.models import Food, Wall, Statistics, Recommendation, Block


@receiver(post_save, sender=Food)
def food_added(sender, instance, **kwargs):
    last_statistic = Statistics.objects.last()
    last_block = Block.objects.last()

    if last_block.day == datetime.datetime.now().date():
        last_block.food.add(instance)
        last_block.save()
    else:
        Block.objects.create(day=datetime.datetime.now().date(),
                             food=instance)

    if last_statistic.day == datetime.datetime.now().date():
        last_statistic.amount += instance.quantity
        last_statistic.save()
    else:
        Statistics.objects.create(day=datetime.datetime.now().date(),
                                  food=instance,
                                  amount=instance.quantity)

# @receiver(post_save, sender=Recommendation)
# def recommendation_added(sender, instance, **kwargs):
#
