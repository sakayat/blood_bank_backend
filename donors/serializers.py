from rest_framework import serializers
from .models import DonorProfile, BloodEventRequest


class DonorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorProfile
        fields = [
            "id",
            "first_name",
            "last_name",
            "age",
            "address",
            "last_donation",
            "available",
        ]


class BloodEventRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodEventRequest
        fields = ["id", "event_des", "blood_group", "accepted_by"]
