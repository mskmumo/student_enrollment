from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Instructor, Semester

# Create your tests here.

class InstructorTests(APITestCase):
    def setUp(self):
        self.instructor_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',  # Ensure this is unique for each test
            'specialization': 'Mathematics'
        }
        self.instructor = Instructor.objects.create(**self.instructor_data)

    def test_create_instructor(self):
        # Use a unique email for the new instructor
        new_instructor_data = {
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com',  # Unique email
            'specialization': 'Physics'
        }
        response = self.client.post(reverse('instructor-list-create'), new_instructor_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_instructor(self):
        response = self.client.get(reverse('instructor-detail', args=[self.instructor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.instructor.name)

    def test_update_instructor(self):
        # Ensure all required fields are included in the update request
        update_data = {
            'name': 'Updated Name',  # Ensure this is valid
            'email': 'john.doe@example.com',  # Include email if required
            'specialization': 'Updated Specialization'  # Ensure this is valid
        }
        
        response = self.client.put(reverse('instructor-detail', args=[self.instructor.id]), update_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instructor.refresh_from_db()
        self.assertEqual(self.instructor.name, 'Updated Name')

    def test_delete_instructor(self):
        response = self.client.delete(reverse('instructor-detail', args=[self.instructor.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Instructor.objects.filter(id=self.instructor.id).exists())


class SemesterTests(APITestCase):
    def setUp(self):
        self.semester_data = {
            'name': 'Fall 2024',
            'start_date': '2024-09-01',
            'end_date': '2024-12-15'
        }
        self.semester = Semester.objects.create(**self.semester_data)

    def test_create_semester(self):
        response = self.client.post(reverse('semester-list-create'), self.semester_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_semester(self):
        response = self.client.get(reverse('semester-detail', args=[self.semester.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.semester.name)

    def test_update_semester(self):
        # Check the data being sent in the update request
        update_data = {
            'name': 'Updated Semester Name',  # Ensure this is valid
            'start_date': '2024-01-01',        # Ensure this is valid
            'end_date': '2024-05-01'           # Ensure this is valid
        }
        
        response = self.client.put(f'/api/semesters/{self.semester.id}/', update_data)
        
        # Check if the response status code is as expected
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # This is failing
        
        self.semester.refresh_from_db()
        self.assertEqual(self.semester.name, 'Updated Semester Name')

    def test_delete_semester(self):
        response = self.client.delete(reverse('semester-detail', args=[self.semester.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Semester.objects.filter(id=self.semester.id).exists())
