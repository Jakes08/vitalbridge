import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import Home from './pages/Home';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Footer from './components/Footer';
import './i18n';

function App() {
    return (
        <AuthProvider>
            <Router>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                </Routes>
                <Footer />
            </Router>
        </AuthProvider>
    );
}

export default App;
// This code is the main entry point of a React application.
// It sets up the routing for the application using React Router.
// The AuthProvider component is used to provide authentication context to the application.
// The application has three main routes: the home page ("/"), the login page ("/login"), and the dashboard page ("/dashboard").