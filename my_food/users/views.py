from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import MainUser, Profile
from users.serializers import MainUserSerializer, ProfileGetSerializer, ProfileSerializer
from users.token import get_token


@api_view(['POST'])
def signup(request):
    serializer = MainUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def login(request):
    username = request.query_params.get('username')
    password = request.query_params.get('password')
    if username is None or password is None:
        raise ValidationError('Please enter credentials')
    try:
        user = MainUser.objects.get(username=username)
        if not user.check_password(password):
            raise ValidationError('Username or password incorrect')
    except MainUser.DoesNotExist:
        raise ValidationError('User doesn\'t exist')
    token = get_token(user)
    return Response({'token': token})


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_serializer_class(self):
        if self.action == 'get_queryset':
            return ProfileGetSerializer
        return ProfileSerializer

    def get_queryset(self):
        return self.queryset.all()

    def update(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        profile.bio = request.data['bio']
        profile.avatar = request.data['avatar']
        profile.save()
        serializer = ProfileGetSerializer(profile)
        return Response(serializer.data)


class MainUserAPIView(APIView):

    def signup(self, request):
        serializer = MainUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def login(self, request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        if email is None or password is None:
            raise ValidationError('Please enter credentials')
        try:
            user = MainUser.objects.get(email=email)
            if not user.check_password(password):
                raise ValidationError('Email or password incorrect')
        except MainUser.DoesNotExist:
            raise ValidationError('Email or password incorrect')
        token = get_token(user)
        return Response({'token': token})

    def get_profile(self, request):
        profile = Profile.objects.get(user_id=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def update_profile(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
