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