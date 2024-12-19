from django.shortcuts import render
from rest_framework import generics
from .models import Student, Course, Enrollment, Instructor, Semester
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    InstructorSerializer,
    SemesterSerializer,
)
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "students_list_create": "/api/students/",
        "student_detail": "/api/students/{id}/",
        "courses_list_create": "/api/courses/",
        "course_detail": "/api/courses/{id}/",
        "enrollments_list_create": "/api/enrollments/",
        "enrollment_detail": "/api/enrollments/{id}/",
        "instructors_list_create": "/api/instructors/",
        "instructor_detail": "/api/instructors/{id}/",
        "semesters_list_create": "/api/semesters/",
        "semester_detail": "/api/semesters/{id}/",
    })

# Student Views
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Enrollment Views
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# Instructor Views
class InstructorListCreateView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# Semester Views
class SemesterListCreateView(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class SemesterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
