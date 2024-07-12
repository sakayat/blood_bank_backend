from rest_framework import serializers
from .models import DonorProfile, BloodRequest


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


class BloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = ["id", "event_des", "blood_group", "accepted_by"]
