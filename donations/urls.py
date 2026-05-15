from django.urls import path
from .views import DonationCreateView, DonationStatsView

urlpatterns = [
    path('', DonationCreateView.as_view(), name='donate'),
    path('stats/', DonationStatsView.as_view(), name='donation-stats'),
]