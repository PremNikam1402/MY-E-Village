from django.db import models


class Service(models.Model):
    """
    Each card in the 'Smart Village Services' section.
    SQL Table: services_service
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/icons/', null=True, blank=True)
    order = models.IntegerField(default=0, help_text="Display order on page")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title