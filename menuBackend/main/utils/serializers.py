from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()


class UserRegistrationSer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, cleaned_data):
        user = UserModel.objects.create_user(email=cleaned_data["email"], password=cleaned_data["password"])
        user.username = cleaned_data["username"]
        user.save()
        return user


class UserLoginSer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def user_login(self, cleaned_data):
        user = authenticate(username=cleaned_data["email"], password=cleaned_data["password"])
        if not user:
            raise ValidationError(f"User {cleaned_data['email']} not found")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')
