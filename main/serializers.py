from rest_framework import serializers
from .models import EducationalModule


class EducationalModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для EducationalModule"""
    class Meta:
        model = EducationalModule
        fields = ['number', 'title', 'description']
        read_only_fields = ['number']
