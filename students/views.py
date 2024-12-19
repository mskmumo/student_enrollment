from django.shortcuts import render
from rest_framework import generics
from .models import Student 
from .serializers import StudentSerializer
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "students_list_create": "/api/students/",
        "student_detail": "/api/students/<int:pk>/",
    })

# Create your views here.

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
