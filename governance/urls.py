from django.urls import path
from .views import CertificateListCreateView, GovernmentSchemeListView

urlpatterns = [
    path('certificates/', CertificateListCreateView.as_view(), name='certificates'),
    path('schemes/', GovernmentSchemeListView.as_view(), name='schemes'),
]