from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from ..utils import validators
from ..utils.serializers import UserRegistrationSer, UserLoginSer, UserSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def user_register(request):
    if request.method == "POST":
        clean_data = validators.clean_data_base(request.data)
        serializer = UserRegistrationSer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([SessionAuthentication])
def user_login(request):
    if request.method == "POST":
        users = User.objects.all()
        for user in users:
            print(user.email, user.username)

        clean_data = validators.clean_data(request.data)
        serializer = UserLoginSer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.user_login(clean_data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes([permissions.IsAuthenticated])
@authentication_classes([SessionAuthentication])
def get_user(request):
    if request.method == 'GET':
        serializer = UserSerializer(data=request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

