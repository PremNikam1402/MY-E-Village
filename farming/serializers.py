from rest_framework import serializers
from .models import FarmProfile, MarketRate


class FarmProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmProfile
        fields = '__all__'
        read_only_fields = ['farmer']


class MarketRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketRate
        fields = '__all__'