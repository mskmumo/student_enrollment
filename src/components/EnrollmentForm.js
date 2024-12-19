import React, { useState } from 'react';

const EnrollmentForm = () => {
    const [enrollment, setEnrollment] = useState({ studentId: '', courseId: '' });

    const handleChange = (e) => {
        setEnrollment({ ...enrollment, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add API call to submit the enrollment data
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="studentId" placeholder="Student ID" onChange={handleChange} />
            <input type="text" name="courseId" placeholder="Course ID" onChange={handleChange} />
            <button type="submit">Enroll Student</button>
        </form>
    );
};

export default EnrollmentForm; 