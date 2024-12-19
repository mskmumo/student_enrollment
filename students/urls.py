from django.urls import path
from .views import (
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
    api_root,
)

urlpatterns = [
    path('', api_root, name='api-root'),  # Add root view for /api/
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
]
