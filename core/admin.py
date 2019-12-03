from django.contrib import admin

from core.models import Food, Compatibility, Recommendation, Wall, Statistics


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'quantity',
        'calories'
    )

    fields = ('name', 'type', 'quantity', 'calories', 'carbs', 'proteins', 'fat')


@admin.register(Compatibility)
class CompatibilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'food1',
        'food2',
        'count'
    )

    fields = ('count', 'food1', 'food2')


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'day',
        'food',
        'amount'
    )

    fields = ('day', 'food', 'amount')


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recommend'
    )

    fields = ('recommend', )


@admin.register(Wall)
class WallAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'statistics'
    )

    fields = ('user', 'statistics')
    readonly_fields = ('user',)
