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
    ("a-positive", "a-positive"),
    ("a-negative", "a-negative"),
    ("b-positive", "b-positive"),
    ("b-negative", "b-negative"),
    ("ab-positive", "ab-positive"),
    ("ab-negative", "ab-negative"),
    ("o-positive", "o-positive"),
    ("o-negative", "o-negative")
]

class BloodRequest(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blood_request")
    blood_group = models.CharField(max_length=20, choices=BLOOD_TYPES)
    location = models.CharField(max_length=100)
    date = models.DateField()
    volume = models.IntegerField()
    event_description = models.TextField()
    status = models.CharField(max_length=20, default="pending")
    
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
    

