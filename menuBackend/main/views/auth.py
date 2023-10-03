from rest_framework import status
from rest_framework.response import Response

from ..utils import validators
from ..utils.serializers import UserRegistrationSer


def user_register(request):
    clean_data = validators.clean_data(request.data)
    serializer = UserRegistrationSer(data=clean_data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.create(clean_data)
        if user:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)