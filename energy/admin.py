from django.contrib import admin
from .models import EnergyProject

@admin.register(EnergyProject)
class EnergyProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_type', 'village', 'status', 'capacity_kw']
    list_filter = ['status', 'project_type']