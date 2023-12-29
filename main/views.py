from rest_framework.viewsets import ModelViewSet

from main.models import EducationalModule
from main.serializers import EducationalModuleSerializer


class EducationalModuleViewSet(ModelViewSet):
    """Контроллер для создания и просмотра экземпляров модели"""
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer
