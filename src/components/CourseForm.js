import React, { useState } from 'react';

const CourseForm = () => {
    const [course, setCourse] = useState({ title: '', code: '', description: '', credits: '' });

    const handleChange = (e) => {
        setCourse({ ...course, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add API call to submit the course data
    };

    return (
        <form onSubmit={handleSubmit} className="form-group">
            <input type="text" name="title" placeholder="Course Title" className="form-control" onChange={handleChange} />
            <input type="text" name="code" placeholder="Course Code" className="form-control" onChange={handleChange} />
            <textarea name="description" placeholder="Course Description" className="form-control" onChange={handleChange}></textarea>
            <input type="number" name="credits" placeholder="Credits" className="form-control" onChange={handleChange} />
            <button type="submit" className="btn btn-primary">Add Course</button>
        </form>
    );
};

export default CourseForm; 