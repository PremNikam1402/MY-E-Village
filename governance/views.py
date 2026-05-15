from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Certificate, GovernmentScheme
from .serializers import CertificateSerializer, GovernmentSchemeSerializer


class CertificateListCreateView(APIView):
    """
    GET  /api/governance/certificates/ — List own certificates
    POST /api/governance/certificates/ — Apply for a certificate
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        certs = Certificate.objects.filter(applicant=request.user)
        serializer = CertificateSerializer(certs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(applicant=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GovernmentSchemeListView(APIView):
    """GET /api/governance/schemes/ — List all active schemes"""

    def get(self, request):
        schemes = GovernmentScheme.objects.filter(is_active=True)
        serializer = GovernmentSchemeSerializer(schemes, many=True)
        return Response(serializer.data)