from django.contrib import admin
from .models import DonorProfile, DonationHistory, BloodRequest


# Register your models here.
admin.site.register(DonorProfile)
admin.site.register(DonationHistory)
admin.site.register(BloodRequest)
