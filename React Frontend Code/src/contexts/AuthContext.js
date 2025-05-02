import React, { createContext, useContext, useState, useEffect } from 'react';
import { auth } from '../firebase';
import { onAuthStateChanged } from 'firebase/auth';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [currentUser, setCurrentUser] = useState(null);

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            setCurrentUser(user);
        });
        return unsubscribe;
    }, []);

    return <AuthContext.Provider value={{ currentUser }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);
// This code defines an authentication context for a React application using Firebase.
// It creates an AuthContext using React's createContext API.
// The AuthProvider component uses the useEffect hook to listen for changes in the authentication state using Firebase's onAuthStateChanged function.
// When the authentication state changes, it updates the currentUser state with the new user object.
// The AuthProvider component wraps its children with the AuthContext.Provider, passing the currentUser as a value.
// The useAuth custom hook allows other components to access the authentication context easily.
// This setup is useful for managing user authentication state throughout the application.
// It allows components to access the current user and respond to authentication state changes.