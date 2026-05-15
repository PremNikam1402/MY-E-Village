from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    seller_name = serializers.CharField(source='seller.username', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'seller_name', 'name', 'description', 'category',
                  'price', 'quantity_available', 'unit', 'image', 'is_available', 'created_at']
        read_only_fields = ['seller_name', 'created_at']


class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_name', 'quantity', 'total_price',
                  'delivery_address', 'status', 'ordered_at']
        read_only_fields = ['total_price', 'status', 'ordered_at']