from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EnergyProject
from .serializers import EnergyProjectSerializer


class EnergyProjectListView(APIView):
    """GET /api/energy/projects/ — All energy projects"""

    def get(self, request):
        projects = EnergyProject.objects.all()
        serializer = EnergyProjectSerializer(projects, many=True)
        return Response(serializer.data)