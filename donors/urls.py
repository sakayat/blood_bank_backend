from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DonorProfileAPI,
    UpdateDonorProfileAPI,
    BloodRequestAPI,
    AcceptBloodRequestAPI,
    CancelBloodRequest,
    DonationHistoryAPI,
    OngoingBloodRequestAPI,
    BloodRequestListAPI,
    DonorListAPI
)

router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("profile/", DonorProfileAPI.as_view(), name="profile"),
    path(
        "update-profile/<int:pk>/", UpdateDonorProfileAPI.as_view(), name="update-donor"
    ),
    path("list/", DonorListAPI.as_view(), name="list"),
    path("blood-request/", BloodRequestAPI.as_view(), name="blood-request"),
    path("request-list/", BloodRequestListAPI.as_view(), name="request-list"),
    path(
        "accept-request/<int:id>/",
        AcceptBloodRequestAPI.as_view(),
        name="accept",
    ),
    path(
        "cancel-request/<int:id>/",
        CancelBloodRequest.as_view(),
        name="cancel",
    ),
    path("donation-history/", DonationHistoryAPI.as_view(), name="donation-history"),
    path("ongoing-requests/", OngoingBloodRequestAPI.as_view(), name="ongoing-requests"),
]
