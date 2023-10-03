from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

UserModel = get_user_model()
PASSWORD_MAX_LEN = 5
def clean_data(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()

    if not email or not UserModel.objects.filter(email=email).exists():
        raise ValidationError("Email not recognized")

    if not password or len(password) <= 5:
        raise ValidationError(f"Choose another password, min length = {PASSWORD_MAX_LEN}")

    if not username:
        raise ValidationError("No username provided")

    return data
