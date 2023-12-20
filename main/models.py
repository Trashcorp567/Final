from django.db import models


class EducationalModule(models.Model):
    """Модель - Образовательные модули"""
    number = models.PositiveIntegerField(default=1, verbose_name='порядковый номер')
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def save(self, *args, **kwargs):
        """Переопределение метода для увеличения порядкового номера"""
        if not self.id:
            last_module = EducationalModule.objects.all().order_by('-number').first()
            if last_module:
                self.number = last_module.number + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модуля"
