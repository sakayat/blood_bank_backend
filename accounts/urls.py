from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistration, UserLogin, UserLogout

router = DefaultRouter()


urlpatterns = [
    path("register/", UserRegistration.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout")
]
