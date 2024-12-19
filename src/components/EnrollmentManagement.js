import React, { useEffect, useState } from 'react';
import EnrollmentForm from './EnrollmentForm';
import EnrollmentList from './EnrollmentList';
import axios from 'axios';

const EnrollmentManagement = () => {
    const [enrollments, setEnrollments] = useState([]);

    const fetchEnrollments = async () => {
        const response = await axios.get('/api/enrollments/');
        setEnrollments(response.data);
    };

    const addEnrollment = async (enrollment) => {
        await axios.post('/api/enrollments/', enrollment);
        fetchEnrollments();
    };

    useEffect(() => {
        fetchEnrollments();
    }, []);

    return (
        <div>
            <h1>Enrollment Management</h1>
            <EnrollmentForm onSubmit={addEnrollment} />
            <EnrollmentList enrollments={enrollments} />
        </div>
    );
};

export default EnrollmentManagement; 