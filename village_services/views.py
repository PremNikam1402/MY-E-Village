from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer


class ServiceListView(APIView):
    """GET /api/services/ — Returns all active services"""

    def get(self, request):
        services = Service.objects.filter(is_active=True)
        serializer = ServiceSerializer(services, many=True, context={'request': request})
        return Response(serializer.data)