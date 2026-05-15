from rest_framework import serializers
from .models import Certificate, GovernmentScheme


class CertificateSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(source='applicant.username', read_only=True)

    class Meta:
        model = Certificate
        fields = ['id', 'applicant_name', 'certificate_type', 'status',
                  'application_date', 'approval_date', 'notes', 'document']
        read_only_fields = ['status', 'application_date', 'approval_date']


class GovernmentSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentScheme
        fields = '__all__'