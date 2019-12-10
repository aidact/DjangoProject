from rest_framework import serializers

from core.models import Wall, Recommendation, Compatibility, Food, Statistics

# from utils.constants import TYPES

TYPES = ['BREAKFAST', 'BRUCNH', 'LUNCH', 'DINNER']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

    def validate_type(self, value):
        if value not in TYPES:
            raise serializers.ValidationError('type options: [BREAKFAST, BRUCNH, LUNCH, DINNER]')
        return value


class CompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Compatibility
        fields = '__all__'

    def validate_food(self, value):
        if value.food1 == value.food2:
            raise serializers.ValidationError('Food must be different')
        return value


class RecommendationSerializer(serializers.Serializer):
    recommend = serializers.CharField(max_length=255)

    def create(self, validated_data):
        task = Recommendation.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        instance.recommend = validated_data.get('recommend', instance.recommend)

        instance.save()
        return instance


class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = '__all__'
        read_only_fields = ('user',)


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'
        read_only_fields = ('user',)
