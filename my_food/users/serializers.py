from rest_framework import serializers
from django.db import transaction
from users.models import MainUser, Profile

# from utils.constants import GENDERS

GENDERS = ['M', 'F', 'None']


class MainUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        # user = MainUser.objects.create_user(**validated_data)

        with transaction.atomic():
            user = MainUser.objects.create_user(**validated_data)
            Profile.objects.create(user=user)
            return user

    def validate_password(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('password is too short')
        return value


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileGetSerializer(serializers.Serializer):
    bio = serializers.CharField(max_length=255)
    avatar = serializers.FileField(allow_null=True)
    user = MainUserSerializer()

    def create(self, validated_data):
        profile = Profile.objects.create(**validated_data)
        return profile

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar = validated_data.get('avatar', instance.avatar)

        instance.save()
        return instance


class MainUserGetSerializer(MainUserSerializer):
    profile = ProfileSerializer()

    class Meta(MainUser.Meta):
        fields = MainUserSerializer.Meta.fields + ('gender', 'age', 'height', 'weight')

    def validate_gender(self, value):
        if value not in GENDERS:
            raise serializers.ValidationError('gender options: [F, M, None]')
        return value
