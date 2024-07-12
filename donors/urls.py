from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonorProfileAPI, UpdateDonorProfileAPI, BloodEventRequestAPI

router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("donor/", DonorProfileAPI.as_view(), name="donor"),
    path("update-donor/<int:pk>/", UpdateDonorProfileAPI.as_view(), name="update-donor"),
    path("blood-event/", BloodEventRequestAPI.as_view(), name="blood-event"),
]
