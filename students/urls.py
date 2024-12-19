from django.urls import path
from .views import (
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
    CourseListCreateView,
    CourseRetrieveUpdateDestroyView,
    EnrollmentListCreateView,
    EnrollmentRetrieveUpdateDestroyView,
    InstructorListCreateView,
    InstructorRetrieveUpdateDestroyView,
    SemesterListCreateView,
    SemesterRetrieveUpdateDestroyView,
    api_root,
)

urlpatterns = [
    path('', api_root, name='api-root'),  # Add root view for /api/
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-detail'),
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('instructors/<int:pk>/', InstructorRetrieveUpdateDestroyView.as_view(), name='instructor-detail'),
    path('semesters/', SemesterListCreateView.as_view(), name='semester-list-create'),
    path('semesters/<int:pk>/', SemesterRetrieveUpdateDestroyView.as_view(), name='semester-detail'),
]
