from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from main.models import EducationalModule
from main.serializers import EducationalModuleSerializer


class EducationalModuleModelTest(TestCase):
    """Тесты для модели"""
    def test_create_educational_module(self):
        """Тест корректного создания модуля."""
        module = EducationalModule.objects.create(
            title='Тестовый модуль',
            description='Тестовое описание'
        )
        self.assertEqual(module.title, 'Тестовый модуль')
        self.assertEqual(module.description, 'Тестовое описание')

    def test_str_method_returns_expected_string(self):
        """Тест указания описания модели после создания"""
        module = EducationalModule(title='Тестовый модуль', description='Тестовое описание')
        expected_str = 'Тестовый модуль - Тестовое описание'
        self.assertEqual(str(module), expected_str)


class EducationalModuleSerializerTest(APITestCase):
    """Тесты сериализатора"""
    def test_serialize_educational_module(self):
        """Проверка сериализатора"""
        module_data = {
            'title': 'Тестовый модуль',
            'description': 'Тестовое описание'
        }
        module_instance = EducationalModule.objects.create(**module_data)
        serializer = EducationalModuleSerializer(instance=module_instance)
        self.assertEqual(serializer.data['title'], 'Тестовый модуль')
        self.assertEqual(serializer.data['description'], 'Тестовое описание')


class EducationalModuleViewsTest(APITestCase):
    """Тесты API запросов"""
    def setUp(self):
        """Создание тестовой модели"""
        self.module_data = {
            'title': 'Тестовый модуль',
            'description': 'Тестовое описание'
        }
        self.module_instance = EducationalModule.objects.create(**self.module_data)
        self.url = f'/api/module/{self.module_instance.id}/'

    def test_retrieve_educational_module(self):
        """Получение данных по модулю"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = EducationalModuleSerializer(instance=self.module_instance)
        self.assertEqual(response.data, serializer.data)

    def test_update_educational_module(self):
        """Обновление данных модуля"""
        updated_data = {
            'title': 'Обновленный модуль',
            'description': 'Обновленное описание'
        }
        response = self.client.patch(self.url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module_instance.refresh_from_db()
        self.assertEqual(self.module_instance.title, 'Обновленный модуль')
        self.assertEqual(self.module_instance.description, 'Обновленное описание')

    def test_delete_educational_module(self):
        """Удаление модуля"""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(EducationalModule.DoesNotExist):
            self.module_instance.refresh_from_db()
