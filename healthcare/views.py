from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer


class DoctorListView(APIView):
    """GET /api/healthcare/doctors/ — List available doctors"""

    def get(self, request):
        doctors = Doctor.objects.filter(is_available=True)
        serializer = DoctorSerializer(doctors, many=True, context={'request': request})
        return Response(serializer.data)


class AppointmentListCreateView(APIView):
    """
    GET  /api/healthcare/appointments/ — My appointments
    POST /api/healthcare/appointments/ — Book appointment
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        appointments = Appointment.objects.filter(patient=request.user)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)