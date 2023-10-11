from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User

UserModel = get_user_model()


class UserRegistrationSer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, cleaned_data):
        user = User.objects.create_user(email=cleaned_data["email"], username=cleaned_data["username"], password=cleaned_data["password"])
        # user.username = cleaned_data["username"]
        user.save()
        return user


class UserLoginSer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def user_login(self, cleaned_data):
        users = User.objects.all()
        user = authenticate(email=cleaned_data["username"], password=cleaned_data["password"])
        if user is not None:
            raise ValidationError(f"User {cleaned_data['username']} not found")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')
