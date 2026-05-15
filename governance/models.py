from django.db import models
from django.contrib.auth.models import User


class Certificate(models.Model):
    """
    Tracks digital certificates issued to citizens.
    SQL Table: governance_certificate
    """
    CERT_TYPES = [
        ('birth', 'Birth Certificate'),
        ('death', 'Death Certificate'),
        ('income', 'Income Certificate'),
        ('domicile', 'Domicile Certificate'),
        ('caste', 'Caste Certificate'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    certificate_type = models.CharField(max_length=20, choices=CERT_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    application_date = models.DateField(auto_now_add=True)
    approval_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    document = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.certificate_type} ({self.status})"


class GovernmentScheme(models.Model):
    """
    Lists all government schemes available to villagers.
    SQL Table: governance_governmentscheme
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    eligibility = models.TextField()
    benefits = models.TextField()
    how_to_apply = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name