import React, { useEffect, useState } from 'react';
import CourseForm from './CourseForm';
import CourseList from './CourseList';
import axios from 'axios';

const CourseManagement = () => {
    const [courses, setCourses] = useState([]);

    const fetchCourses = async () => {
        const response = await axios.get('/api/courses/');
        setCourses(response.data);
    };

    const addCourse = async (course) => {
        await axios.post('/api/courses/', course);
        fetchCourses();
    };

    const updateCourse = async (id, course) => {
        await axios.put(`/api/courses/${id}/`, course);
        fetchCourses();
    };

    const deleteCourse = async (id) => {
        await axios.delete(`/api/courses/${id}/`);
        fetchCourses();
    };

    useEffect(() => {
        fetchCourses();
    }, []);

    return (
        <div>
            <h1>Course Management</h1>
            <CourseForm onSubmit={addCourse} />
            <CourseList courses={courses} onUpdate={updateCourse} onDelete={deleteCourse} />
        </div>
    );
};

export default CourseManagement; 