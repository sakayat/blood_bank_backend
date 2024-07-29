from rest_framework import serializers
from .models import Donor, BloodRequest, DonationHistory

class DonorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="donor.email", read_only=True)
    class Meta:
        model = Donor
        fields = [
            "id",
            "first_name",
            "last_name",
            "blood_group",
            "gender",
            "religion",
            "email",
            "age",
            "profession",
            "address",
            "last_donation",
            "is_available",
        ]
    
    


class BloodRequestSerializer(serializers.ModelSerializer):
    donor = serializers.StringRelatedField()
    class Meta:
        model = BloodRequest
        fields = [
            "id",
            "donor",
            "blood_group",
            "units",
            "location",
            "event_description",
            "contact",
            "status",
            "createdAt"
        ]
        read_only_fields = ["id", "donor", "status"]



class DonationHistorySerializer(serializers.ModelSerializer):
    donor = serializers.ReadOnlyField(source="donor.username")
    recipient = serializers.ReadOnlyField(source="recipient.username")
    class Meta:
        model = DonationHistory
        fields = ["id", "donor", "recipient", "status", "created_at"]