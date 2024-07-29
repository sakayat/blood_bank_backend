from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DonorProfileAPI,
    UpdateDonorProfileAPI,
    AcceptBloodRequestAPI,
    CancelBloodRequest,
    DonationHistoryAPI,
    OngoingBloodRequestAPI,
    DonorListAPI,
    AllBloodRequestViewSet,
    BloodRequestViewSet,
    BloodTypesAPI,
    DonorDetailsAPI
)

router = DefaultRouter()

router.register("blood-request", BloodRequestViewSet, basename="blood-request")
router.register("blood-request-list", AllBloodRequestViewSet, basename="blood-request-list")
router.register("ongoing-requests", OngoingBloodRequestAPI, basename="ongoing-requests")

urlpatterns = [
    path("", include(router.urls)),
    path("profile/", DonorProfileAPI.as_view(), name="profile"),
    path(
        "update-profile/<int:pk>/", UpdateDonorProfileAPI.as_view(), name="update-donor"
    ),
    path("list/", DonorListAPI.as_view(), name="list"),
    path("details/<int:pk>/", DonorDetailsAPI.as_view(), name="list"),
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
    # path("ongoing-requests/", OngoingBloodRequestAPI.as_view(), name="ongoing-requests"),
    path("bloods/", BloodTypesAPI.as_view(), name="bloods"),
]
