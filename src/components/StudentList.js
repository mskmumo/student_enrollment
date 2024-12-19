import React, { useEffect, useState } from 'react';

const StudentList = () => {
    const [students, setStudents] = useState([]);
    const [sortConfig, setSortConfig] = useState(null);

    useEffect(() => {
        // Fetch students from the API
    }, []);

    const sortedStudents = React.useMemo(() => {
        let sortableStudents = [...students];
        if (sortConfig !== null) {
            sortableStudents.sort((a, b) => {
                if (a[sortConfig.key] < b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? -1 : 1;
                }
                if (a[sortConfig.key] > b[sortConfig.key]) {
                    return sortConfig.direction === 'ascending' ? 1 : -1;
                }
                return 0;
            });
        }
        return sortableStudents;
    }, [students, sortConfig]);

    const requestSort = (key) => {
        let direction = 'ascending';
        if (sortConfig && sortConfig.key === key && sortConfig.direction === 'ascending') {
            direction = 'descending';
        }
        setSortConfig({ key, direction });
    };

    return (
        <div>
            <h1>Students</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th onClick={() => requestSort('firstName')}>First Name</th>
                        <th onClick={() => requestSort('lastName')}>Last Name</th>
                        <th onClick={() => requestSort('email')}>Email</th>
                    </tr>
                </thead>
                <tbody>
                    {sortedStudents.map(student => (
                        <tr key={student.id}>
                            <td>{student.firstName}</td>
                            <td>{student.lastName}</td>
                            <td>{student.email}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default StudentList; 