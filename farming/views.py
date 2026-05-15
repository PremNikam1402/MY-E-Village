from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FarmProfile, MarketRate
from .serializers import FarmProfileSerializer, MarketRateSerializer


class MarketRateListView(APIView):
    """GET /api/farming/market-rates/ — Today's crop prices"""

    def get(self, request):
        rates = MarketRate.objects.all()[:20]
        serializer = MarketRateSerializer(rates, many=True)
        return Response(serializer.data)


class FarmProfileView(APIView):
    """GET/POST /api/farming/profile/ — Farmer's profile"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            farm = FarmProfile.objects.get(farmer=request.user)
            return Response(FarmProfileSerializer(farm).data)
        except FarmProfile.DoesNotExist:
            return Response({'error': 'No farm profile found'}, status=404)

    def post(self, request):
        serializer = FarmProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(farmer=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)