from django.contrib import admin
from .models import Certificate, GovernmentScheme

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'certificate_type', 'status', 'application_date']
    list_filter = ['status', 'certificate_type']
    search_fields = ['applicant__username']

@admin.register(GovernmentScheme)
class GovernmentSchemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'deadline', 'is_active']