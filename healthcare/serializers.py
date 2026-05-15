from rest_framework import serializers
from .models import Doctor, Appointment


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'experience_years',
                  'photo', 'available_days', 'consultation_fee', 'is_available']


class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.username', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient_name', 'doctor', 'doctor_name', 'appointment_date',
                  'appointment_time', 'symptoms', 'status', 'prescription', 'created_at']
        read_only_fields = ['status', 'prescription']