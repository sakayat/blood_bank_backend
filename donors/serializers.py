from rest_framework import serializers
from .models import DonorProfile


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
