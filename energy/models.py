from django.db import models


class EnergyProject(models.Model):
    """
    Solar/clean energy projects in villages.
    SQL Table: energy_energyproject
    """
    TYPE_CHOICES = [
        ('solar', 'Solar Power'),
        ('wind', 'Wind Energy'),
        ('biogas', 'Biogas'),
        ('hydro', 'Micro Hydro'),
    ]
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    project_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    village = models.CharField(max_length=100)
    capacity_kw = models.DecimalField(max_digits=8, decimal_places=2, help_text="Capacity in kilowatts")
    beneficiary_count = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    start_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.village})"