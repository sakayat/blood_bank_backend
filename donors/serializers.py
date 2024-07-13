from rest_framework import serializers
from .models import DonorProfile, BloodRequest, DonationHistory


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
        fields = [
            "id",
            "donor",
            "blood_group",
            "location",
            "date",
            "volume",
            "event_description",
            "status",
        ]
        read_only_fields = ["id", "donor", "status"]

class DonationHistorySerializer(serializers.ModelSerializer):
    donor = serializers.ReadOnlyField(source="donor.username")
    recipient = serializers.ReadOnlyField(source="recipient.username")
    class Meta:
        model = DonationHistory
        fields = ["id", "donor", "recipient", "status", "created_at"]