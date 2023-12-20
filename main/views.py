from rest_framework import generics

from main.models import EducationalModule
from main.serializers import EducationalModuleSerializer


class EducationalModuleListCreateView(generics.ListCreateAPIView):
    """Контроллер для создания и просмотра экземпляров модели"""
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer


class EducationalModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Контроллер для редактирования экземпляра модели"""
    queryset = EducationalModule.objects.all()
    serializer_class = EducationalModuleSerializer

    def get_object(self):
        """Переопределение метода для получения объекта"""
        number = self.kwargs['number']
        return EducationalModule.objects.get(number=number)
