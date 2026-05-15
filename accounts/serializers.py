from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    role = serializers.CharField(write_only=True, default='citizen')
    village = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role', 'village']

    def create(self, validated_data):
        role = validated_data.pop('role', 'citizen')
        village = validated_data.pop('village', '')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, role=role, village=village)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'role', 'village', 'phone', 'address', 'profile_picture']