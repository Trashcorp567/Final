from django.contrib import admin

from main.models import EducationalModule


# Register your models here.
@admin.register(EducationalModule)
class EducationalModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'title', 'description')
