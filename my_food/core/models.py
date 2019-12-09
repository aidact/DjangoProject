from django.db import models

from users.models import MainUser
from utils.constants import TYPES, BREAKFAST


class Food(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPES, default=BREAKFAST)
    calories = models.FloatField(null=True)
    carbs = models.FloatField(null=True)
    proteins = models.FloatField(null=True)
    fat = models.FloatField(null=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Food'

    def __str__(self):
        return f'{self.name}: {self.type}, {self.quantity}'


class Statistics(models.Model):
    day = models.DateField(null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='statistics', null=True)
    amount = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'

    def __str__(self):
        return f'{self.day}, {self.amount}'


class Recommendation(models.Model):
    # user = models.ForeignKey(MainUser, related_name='recommend')
    recommend = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'

    def __str__(self):
        return f'{self.recommend}'


class Compatibility(models.Model):
    food1 = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='compatibility1')
    food2 = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='compatibility2')
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Compatibility'
        verbose_name_plural = 'Compatibilities'

    def __str__(self):
        return f'{self.count}'


class Block(models.Model):
    day = models.DateField(null=True)
    food = models.ManyToManyField(Food, related_name='block')
    water = models.IntegerField(null=True, blank=True)
    recommendation = models.ForeignKey(Recommendation, null=True, blank=True, on_delete=models.CASCADE, related_name='block')
    compatibility = models.ManyToManyField(Compatibility, null=True, blank=True)

    class Meta:
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'
        abstract = True

    def __str__(self):
        return f'{self.water}, {self.food}'


class Wall(Block):
    statistics = models.ForeignKey(Statistics, on_delete=models.CASCADE, related_name='wall')
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Wall'
        verbose_name_plural = 'Walls'

    def __str__(self):
        return f'{self.user}: {self.statistics}'
