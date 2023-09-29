from django.urls import path
from .views import gen

urlpatterns = [
    path("check/", gen.check, name="testing")
]