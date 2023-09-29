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
