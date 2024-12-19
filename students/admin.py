from django.contrib import admin
from .models import Student, Course, Instructor, Semester, Enrollment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Semester)
admin.site.register(Enrollment)
