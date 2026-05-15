from rest_framework import serializers
from .models import EnergyProject


class EnergyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyProject
        fields = '__all__'