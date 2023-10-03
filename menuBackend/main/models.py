from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bookings(models.Model):
    name = models.CharField(max_length=100)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()
    # CSV values for different branches; can be left empty to represent just one branch
    restaurant = models.CharField(max_length=1000, default="")
    party_size = models.IntegerField(default=2)
    date = models.DateField(auto_now_add=True)


class MenuUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email or not password:
            ValueError("Provide valid inputs for user creation")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user


