from django.urls import path
from .views import gen, auth

urlpatterns = [
    path("login/", auth.user_login, name="login"),
    path("signup/", auth.user_register, name="register"),
    path("user/", auth.get_user, name="get_user")
]