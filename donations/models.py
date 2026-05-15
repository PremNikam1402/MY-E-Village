from django.db import models
from django.contrib.auth.models import User


class Donation(models.Model):
    """
    Tracks donations made to village projects.
    SQL Table: donations_donation
    """
    PURPOSE_CHOICES = [
        ('education', 'Smart Education'),
        ('healthcare', 'Health Care'),
        ('energy', 'Clean Energy'),
        ('farming', 'Digital Farming'),
        ('general', 'General Village Fund'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    donor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='donations')
    donor_name = models.CharField(max_length=100)         # For anonymous donations
    donor_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='general')
    message = models.TextField(blank=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"₹{self.amount} by {self.donor_name} for {self.purpose}"