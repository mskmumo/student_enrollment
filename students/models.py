from django.db import models

# Create your models here.

# Student Model Class
class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email Address", db_index=True)
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Enrollment Date")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']  # Default ordering by last name, then first name


# Course Model Class
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Course Title")
    code = models.CharField(max_length=10, unique=True, verbose_name="Course Code", db_index=True)
    description = models.TextField(verbose_name="Course Description")
    credits = models.IntegerField(verbose_name="Credits")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # Default ordering by title


# Enrollment Model Class
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Enrollment Date")

    class Meta:
        unique_together = ('student', 'course')  # Ensure a student can enroll in a course only once
        ordering = ['enrollment_date']  # Default ordering by enrollment date


# Instructor Model Class
class Instructor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Instructor Name")
    email = models.EmailField(unique=True, verbose_name="Email Address", db_index=True)
    specialization = models.CharField(max_length=100, verbose_name="Specialization")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Default ordering by name


# Semester Model Class
class Semester(models.Model):
    name = models.CharField(max_length=100, verbose_name="Semester Name")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_date']  # Default ordering by start date