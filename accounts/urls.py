from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistration

router = DefaultRouter()


urlpatterns = [
    path("register/", UserRegistration.as_view(), name="register")
]
