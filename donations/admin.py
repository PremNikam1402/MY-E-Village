from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'amount', 'purpose', 'status', 'donated_at']
    list_filter = ['purpose', 'status']