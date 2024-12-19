import React, { useEffect, useState } from 'react';

const CourseList = () => {
    const [courses, setCourses] = useState([]);
    const [sortConfig, setSortConfig] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchCourses = async () => {
            try {
                const response = await fetch('/api/courses/');
                const data = await response.json();
                setCourses(data);
            } catch (error) {
                console.error('Error fetching courses:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchCourses();
    }, []);

    const sortedCourses = React.useMemo(() => {
        let sortableCourses = [...courses];
        if (sortConfig !== null) {
            sortableCourses.sort((a, b) => {
                if (a[sortConfig.key] < b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? -1 : 1;
                }
                if (a[sortConfig.key] > b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? 1 : -1;
                }
                return 0;
            });
        }
        return sortableCourses;
    }, [courses, sortConfig]);

    const requestSort = (key) => {
        let direction = 'ascending';
        if (sortConfig && sortConfig.key === key && sortConfig.direction === 'ascending') {
            direction = 'descending';
        }
        setSortConfig({ key, direction });
    };

    if (loading) return <p>Loading courses...</p>;

    return (
        <div>
            <h1>Courses</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th onClick={() => requestSort('title')}>Title</th>
                        <th onClick={() => requestSort('code')}>Code</th>
                        <th onClick={() => requestSort('credits')}>Credits</th>
                    </tr>
                </thead>
                <tbody>
                    {sortedCourses.map(course => (
                        <tr key={course.id}>
                            <td>{course.title}</td>
                            <td>{course.code}</td>
                            <td>{course.credits}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CourseList; 