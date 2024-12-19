# Project Outline: Student Enrollment System

## 1. Models

We’ll design at least **5 models** for the system:

- **Student**: `Name`, `ID`, `age`, `email`, `address`.
- **Course**: `Title`, `code`, `description`, `credits`.
- **Enrollment**: Links students to courses with fields like `enrollment date`.
- **Instructor**: `Name`, `ID`, `email`, `specialization`.
- **Semester**: `Name` (e.g., Fall 2024), `start date`, `end date`.

### Relationships:
- A student can enroll in multiple courses.
- An instructor can teach multiple courses.
- A course is associated with a specific semester.

---

## 2. Serializers

For each model, we’ll create a serializer to:
- Convert model instances to JSON and vice versa.
- Add validation rules (e.g., email format, unique course codes).

---

## 3. Views/Viewsets

We’ll implement **CRUD operations** for each model:

- **GET**: Fetch student/course details.
- **POST**: Add new students, courses, or enrollments.
- **PUT/PATCH**: Update existing data.
- **DELETE**: Remove a student or a course.

We’ll use **viewsets** to keep it modular and leverage Django REST Framework's generic classes.

---

## 4. URLs

We’ll create **RESTful URLs** like:

- `/students/`: List and create students.
- `/students/<id>/`: Retrieve, update, or delete a specific student.
- `/courses/`: Manage courses.
- `/enrollments/`: Manage student enrollments.

These URLs will be linked from the project’s main `urls.py` file.

---

## 5. Testing

We’ll:
- Write **unit tests** for all endpoints using `APITestCase`.
- Test CRUD operations with tools like **Postman** and document results:
  - Screenshots for manual tests.
  - Output logs from Django test cases.

---

## 6. Deliverables

### GitHub Repository
- Named `<student_enrollment>`.

### README File
Includes:
- Model descriptions and relationships.
- Explanation of serializers, views, and URLs.
- Test results and screenshots.

### Testing Evidence
- Screenshots or test logs.



## API Endpoints

### Students
- **GET /api/students/**: List all students.
- **POST /api/students/**: Create a new student.
- **GET /api/students/{id}/**: Retrieve a specific student.
- **PUT /api/students/{id}/**: Update a specific student.
- **DELETE /api/students/{id}/**: Delete a specific student.

### Courses
- **GET /api/courses/**: List all courses.
- **POST /api/courses/**: Create a new course.
- **GET /api/courses/{id}/**: Retrieve a specific course.
- **PUT /api/courses/{id}/**: Update a specific course.
- **DELETE /api/courses/{id}/**: Delete a specific course.

### Enrollments
- **GET /api/enrollments/**: List all enrollments.
- **POST /api/enrollments/**: Create a new enrollment.
- **GET /api/enrollments/{id}/**: Retrieve a specific enrollment.
- **PUT /api/enrollments/{id}/**: Update a specific enrollment.
- **DELETE /api/enrollments/{id}/**: Delete a specific enrollment.

### Instructors
- **GET /api/instructors/**: List all instructors.
- **POST /api/instructors/**: Create a new instructor.
- **GET /api/instructors/{id}/**: Retrieve a specific instructor.
- **PUT /api/instructors/{id}/**: Update a specific instructor.
- **DELETE /api/instructors/{id}/**: Delete a specific instructor.

### Semesters
- **GET /api/semesters/**: List all semesters.
- **POST /api/semesters/**: Create a new semester.
- **GET /api/semesters/{id}/**: Retrieve a specific semester.
- **PUT /api/semesters/{id}/**: Update a specific semester.
- **DELETE /api/semesters/{id}/**: Delete a specific semester.