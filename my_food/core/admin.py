import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
from django.db.models.functions import TruncDay

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

    def changelist_view(self, request, extra_context=None):
        chart_data = (
            Statistics.objects.annotate(date=TruncDay("day"))
                .values("date")
                .annotate(y=F("amount"))
                .order_by("-date")
        )

        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recommend'
    )

    fields = ('recommend',)


@admin.register(Wall)
class WallAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'statistics'
    )

    fields = ('user', 'statistics')
    readonly_fields = ('user',)
