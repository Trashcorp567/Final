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
            number=1,
            title='Тестовый модуль',
            description='Тестовое описание'
        )
        self.assertEqual(module.number, 1)
        self.assertEqual(module.title, 'Тестовый модуль')
        self.assertEqual(module.description, 'Тестовое описание')

    def test_save_method_sets_number_correctly(self):
        """Тест указания корректного порядкового номера"""
        module1 = EducationalModule(title='Тестовый модуль 1', description='Тестовое описание 1')
        module1.save()

        module2 = EducationalModule(title='Тестовый модуль 2', description='Тестовое описание 2')
        module2.save()

        self.assertEqual(module1.number, 1)
        self.assertEqual(module2.number, 2)

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
            'number': 1,
            'title': 'Тестовый модуль',
            'description': 'Тестовое описание'
        }
        module_instance = EducationalModule.objects.create(**module_data)
        serializer = EducationalModuleSerializer(instance=module_instance)
        self.assertEqual(serializer.data['number'], 1)
        self.assertEqual(serializer.data['title'], 'Тестовый модуль')
        self.assertEqual(serializer.data['description'], 'Тестовое описание')


class EducationalModuleViewsTest(APITestCase):
    """Тесты API запросов"""
    def setUp(self):
        """Создания тестовой модели"""
        self.module_data = {
            'number': 1,
            'title': 'Тестовый модуль',
            'description': 'Тестовое описание'
        }
        self.module_instance = EducationalModule.objects.create(**self.module_data)
        self.url = f'/api/modules/{self.module_instance.number}/'

    def test_retrieve_educational_module(self):
        """Получение данных по модулю"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = EducationalModuleSerializer(instance=self.module_instance)
        self.assertEqual(response.data, serializer.data)

    def test_update_educational_module(self):
        """Обновление данных модуля"""
        updated_data = {
            'title': 'Обновлённый модуль',
            'description': 'Обновлённое описание'
        }
        response = self.client.patch(self.url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module_instance.refresh_from_db()
        self.assertEqual(self.module_instance.title, 'Обновлённый модуль')
        self.assertEqual(self.module_instance.description, 'Обновлённое описание')

    def test_delete_educational_module(self):
        """Удаление модуля"""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(EducationalModule.DoesNotExist):
            self.module_instance.refresh_from_db()
