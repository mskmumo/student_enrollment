import React, { createContext, useReducer } from 'react';

const initialState = {
    students: [],
    courses: [],
    enrollments: [],
};

const GlobalContext = createContext(initialState);

const GlobalProvider = ({ children }) => {
    const [state, dispatch] = useReducer((state, action) => {
        switch (action.type) {
            case 'SET_STUDENTS':
                return { ...state, students: action.payload };
            case 'SET_COURSES':
                return { ...state, courses: action.payload };
            case 'SET_ENROLLMENTS':
                return { ...state, enrollments: action.payload };
            default:
                return state;
        }
    }, initialState);

    return (
        <GlobalContext.Provider value={{ state, dispatch }}>
            {children}
        </GlobalContext.Provider>
    );
};

export { GlobalContext, GlobalProvider }; 