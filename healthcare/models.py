from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    """
    Doctors available via tele-medicine.
    SQL Table: healthcare_doctor
    """
    SPECIALIZATION_CHOICES = [
        ('general', 'General Physician'),
        ('pediatrics', 'Pediatrics'),
        ('gynecology', 'Gynecology'),
        ('orthopedics', 'Orthopedics'),
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    experience_years = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='doctors/', null=True, blank=True)
    available_days = models.CharField(max_length=200, help_text="e.g. Mon, Wed, Fri")
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"


class Appointment(models.Model):
    """
    Tele-medicine appointments booked by citizens.
    SQL Table: healthcare_appointment
    """
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    symptoms = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    prescription = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} → Dr.{self.doctor.name} on {self.appointment_date}"