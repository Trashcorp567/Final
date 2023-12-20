from django.urls import path
from main.views import EducationalModuleListCreateView, EducationalModuleDetailView

urlpatterns = [
    path('modules/', EducationalModuleListCreateView.as_view(), name='module-list-create'),
    path('modules/<int:number>/', EducationalModuleDetailView.as_view(), name='module-detail'),
]
