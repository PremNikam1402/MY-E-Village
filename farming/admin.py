from django.contrib import admin
from .models import FarmProfile, MarketRate

@admin.register(FarmProfile)
class FarmProfileAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'land_area_acres', 'current_crop', 'location']

@admin.register(MarketRate)
class MarketRateAdmin(admin.ModelAdmin):
    list_display = ['crop_name', 'price_per_kg', 'market_location', 'date']