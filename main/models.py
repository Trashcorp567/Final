from django.db import models


class EducationalModule(models.Model):
    """Модель - Образовательные модули"""
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модуля"
