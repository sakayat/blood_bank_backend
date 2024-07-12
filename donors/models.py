from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DonorProfile(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    address = models.TextField()
    last_donation = models.DateField()
    available = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.donor.username


BLOOD_TYPES = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
]

class BloodRequest(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blood_request")
    blood_group = models.CharField(max_length=5, choices=BLOOD_TYPES)
    des = models.TextField()
    accepted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, default="pending")
    
    def __str__(self) -> str:
        return f"{self.donor.first_name}"
