from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Role, UserRole

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'is_active']

class UserRoleSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'role', 'is_active']

class CustomUserSerializer(serializers.ModelSerializer):
    roles = UserRoleSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'roles']