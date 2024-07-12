from django.contrib import admin
from .models import DonorProfile, DonationHistory


# Register your models here.
admin.site.register(DonorProfile)
admin.site.register(DonationHistory)
