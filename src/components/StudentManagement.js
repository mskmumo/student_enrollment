import React, { useEffect, useState } from 'react';
import StudentForm from './StudentForm';
import StudentList from './StudentList';
import axios from 'axios';

const StudentManagement = () => {
    const [students, setStudents] = useState([]);

    const fetchStudents = async () => {
        const response = await axios.get('/api/students/');
        setStudents(response.data);
    };

    const addStudent = async (student) => {
        await axios.post('/api/students/', student);
        fetchStudents();
    };

    const updateStudent = async (id, student) => {
        await axios.put(`/api/students/${id}/`, student);
        fetchStudents();
    };

    const deleteStudent = async (id) => {
        await axios.delete(`/api/students/${id}/`);
        fetchStudents();
    };

    useEffect(() => {
        fetchStudents();
    }, []);

    return (
        <div>
            <h1>Student Management</h1>
            <StudentForm onSubmit={addStudent} />
            <StudentList students={students} onUpdate={updateStudent} onDelete={deleteStudent} />
        </div>
    );
};

export default StudentManagement; 