from django.db import models
from django.contrib.auth.models import User

BLOOD_TYPES = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-")
]

# Create your models here.
class Donor(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=3, choices=BLOOD_TYPES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")], blank=True, null=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField()
    profession = models.CharField(max_length=20, blank=True, null=True)
    last_donation = models.DateField()
    is_available = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.donor.username


class BloodRequest(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blood_request")
    blood_group = models.CharField(max_length=3, choices=BLOOD_TYPES)
    units = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    event_description = models.TextField()
    contact = models.CharField(max_length=15, unique=True, null=True, blank=True)
    status = models.CharField(max_length=20, default="pending")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"Re{self.donor.username}"

STATUS = [
    ("accepted", "Accepted"),
    ("canceled", "Canceled")
]

class DonationHistory(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipient")
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Donar Name {self.donor.username} Recipient Name {self.recipient.username}"
    

