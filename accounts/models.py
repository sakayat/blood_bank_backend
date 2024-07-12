from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class DonorProfile(AbstractUser):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    last_donation = models.DateField(blank=True, null=True)
    available = models.BooleanField(default=False)