from django.urls import path
from .views import ProductListCreateView, OrderListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='products'),
    path('orders/', OrderListCreateView.as_view(), name='orders'),
]