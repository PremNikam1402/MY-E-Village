from django.db import models
from django.contrib.auth.models import User


class FarmProfile(models.Model):
    """
    Farmer's land and crop data.
    SQL Table: farming_farmprofile
    """
    farmer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farm')
    land_area_acres = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=200)
    soil_type = models.CharField(max_length=100, blank=True)
    water_source = models.CharField(max_length=100, blank=True)
    current_crop = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer.username}'s Farm"


class MarketRate(models.Model):
    """
    Daily market rates for various crops/commodities.
    SQL Table: farming_marketrate
    """
    crop_name = models.CharField(max_length=100)
    price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    market_location = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    source = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.crop_name} - ₹{self.price_per_kg}/kg on {self.date}"