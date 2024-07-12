from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonorProfileAPI, UpdateDonorProfileAPI

router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("donor-profile/", DonorProfileAPI.as_view(), name="donor-profile"),
    path("update-donor-profile/<int:pk>/", UpdateDonorProfileAPI.as_view(), name="update-donor-profile"),
]
