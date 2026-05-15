from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'village', 'phone']
    list_filter = ['role', 'village']
    search_fields = ['user__username', 'user__email']