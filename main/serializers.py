from rest_framework import serializers
from .models import EducationalModule


class EducationalModuleSerializer(serializers.ModelSerializer):
    """Сериализатор для EducationalModule"""
    class Meta:
        model = EducationalModule
        fields = '__all__'
