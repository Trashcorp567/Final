from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import EducationalModuleViewSet

router = DefaultRouter()
router.register(r'module', EducationalModuleViewSet, basename='module')
urlpatterns = router.urls
