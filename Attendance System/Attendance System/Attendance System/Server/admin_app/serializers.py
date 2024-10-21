from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password']) # type: ignore
        return super().create(validated_data)
