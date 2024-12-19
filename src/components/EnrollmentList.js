import React, { useEffect, useState } from 'react';

const EnrollmentList = () => {
    const [enrollments, setEnrollments] = useState([]);
    const [sortConfig, setSortConfig] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchEnrollments = async () => {
            try {
                const response = await fetch('/api/enrollments/');
                const data = await response.json();
                setEnrollments(data);
            } catch (error) {
                console.error('Error fetching enrollments:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchEnrollments();
    }, []);

    const sortedEnrollments = React.useMemo(() => {
        let sortableEnrollments = [...enrollments];
        if (sortConfig !== null) {
            sortableEnrollments.sort((a, b) => {
                if (a[sortConfig.key] < b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? -1 : 1;
                }
                if (a[sortConfig.key] > b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? 1 : -1;
                }
                return 0;
            });
        }
        return sortableEnrollments;
    }, [enrollments, sortConfig]);

    const requestSort = (key) => {
        let direction = 'ascending';
        if (sortConfig && sortConfig.key === key && sortConfig.direction === 'ascending') {
            direction = 'descending';
        }
        setSortConfig({ key, direction });
    };

    if (loading) return <p>Loading enrollments...</p>;

    return (
        <div>
            <h1>Enrollments</h1>
            <table>
                <thead>
                    <tr>
                        <th onClick={() => requestSort('studentId')}>Student ID</th>
                        <th onClick={() => requestSort('courseId')}>Course ID</th>
                        <th onClick={() => requestSort('enrollmentDate')}>Enrollment Date</th>
                    </tr>
                </thead>
                <tbody>
                    {sortedEnrollments.map(enrollment => (
                        <tr key={enrollment.id}>
                            <td>{enrollment.studentId}</td>
                            <td>{enrollment.courseId}</td>
                            <td>{enrollment.enrollmentDate}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default EnrollmentList; 