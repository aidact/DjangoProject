from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from users.models import MainUser
from users.serializers import MainUserSerializer
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
        print(user.password)
        if user.check_password(password):
            raise ValidationError('Username or password incorrect')
    except MainUser.DoesNotExist:
        raise ValidationError('User doesn\'t exist')
    token = get_token(user)
    return Response({'token': token})
