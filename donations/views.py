from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Donation
from .serializers import DonationSerializer


class DonationCreateView(APIView):
    """POST /api/donations/ — Make a donation"""

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            donation = serializer.save()
            if request.user.is_authenticated:
                donation.donor = request.user
                donation.save()
            return Response({
                'message': 'Thank you for your donation!',
                'donation_id': donation.id,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DonationStatsView(APIView):
    """GET /api/donations/stats/ — Total donation statistics"""

    def get(self, request):
        from django.db.models import Sum
        total = Donation.objects.filter(status='completed').aggregate(Sum('amount'))
        count = Donation.objects.filter(status='completed').count()
        return Response({
            'total_amount': total['amount__sum'] or 0,
            'donor_count': count,
        })