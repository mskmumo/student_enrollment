import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import StudentManagement from './components/StudentManagement';
import CourseManagement from './components/CourseManagement';
import EnrollmentManagement from './components/EnrollmentManagement';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/students" element={<StudentManagement />} />
                <Route path="/courses" element={<CourseManagement />} />
                <Route path="/enrollments" element={<EnrollmentManagement />} />
            </Routes>
        </Router>
    );
}

export default App; 