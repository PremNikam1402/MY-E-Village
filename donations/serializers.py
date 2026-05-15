from rest_framework import serializers
from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donor_name', 'donor_email', 'amount', 'purpose',
                  'message', 'status', 'donated_at']
        read_only_fields = ['status', 'donated_at']