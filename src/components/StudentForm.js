import React, { useState } from 'react';

const StudentForm = () => {
    const [student, setStudent] = useState({ firstName: '', lastName: '', email: '' });

    const handleChange = (e) => {
        setStudent({ ...student, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add API call to submit the student data
    };

    return (
        <form onSubmit={handleSubmit} className="form-group">
            <input type="text" name="firstName" placeholder="First Name" className="form-control" onChange={handleChange} />
            <input type="text" name="lastName" placeholder="Last Name" className="form-control" onChange={handleChange} />
            <input type="email" name="email" placeholder="Email" className="form-control" onChange={handleChange} />
            <button type="submit" className="btn btn-primary">Add Student</button>
        </form>
    );
};

export default StudentForm; 