from django.contrib import admin
from .models import Donor, DonationHistory, BloodRequest


# Register your models here.
admin.site.register(Donor)
admin.site.register(DonationHistory)
admin.site.register(BloodRequest)
