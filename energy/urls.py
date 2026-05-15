from django.urls import path
from .views import EnergyProjectListView

urlpatterns = [
    path('projects/', EnergyProjectListView.as_view(), name='energy-projects'),
]