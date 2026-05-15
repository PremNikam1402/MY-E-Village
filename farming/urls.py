from django.urls import path
from .views import MarketRateListView, FarmProfileView

urlpatterns = [
    path('market-rates/', MarketRateListView.as_view(), name='market-rates'),
    path('profile/', FarmProfileView.as_view(), name='farm-profile'),
]