import React from 'react';
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth';

export default function Login() {
    const handleLogin = (e) => {
        e.preventDefault();
        const email = e.target.email.value;
        const password = e.target.password.value;
        const auth = getAuth();
        signInWithEmailAndPassword(auth, email, password)
            .then(userCredential => console.log('Logged in:', userCredential.user))
            .catch(error => console.error('Login error:', error));
    };

    return (
        <form onSubmit={handleLogin} className="p-8 max-w-md mx-auto">
            <input name="email" placeholder="Email" className="block w-full mb-2 p-2 border" required />
            <input name="password" type="password" placeholder="Password" className="block w-full mb-4 p-2 border" required />
            <button type="submit" className="w-full p-2 bg-blue-600 text-white rounded">Login</button>
        </form>
    );
}
// This code defines a React functional component called Login.
// It imports necessary functions from Firebase for authentication.
// The handleLogin function is triggered when the form is submitted.
// It prevents the default form submission behavior, retrieves the email and password from the form fields, and uses Firebase's signInWithEmailAndPassword function to log in the user.
// If the login is successful, it logs the user information to the console.
// If there is an error during login, it logs the error to the console.
// The component renders a simple login form with email and password input fields and a submit button.
// The form is styled using Tailwind CSS classes for a clean and modern look.
// The email and password fields are required, ensuring that the user cannot submit the form without providing them.
// The component is exported as the default export, making it available for use in other parts of the application.
// The Firebase authentication functions allow for easy integration of user authentication in the application.
// The component can be further enhanced with error handling and user feedback for a better user experience.
// The form is styled with Tailwind CSS classes for a modern and responsive design.
// The login button is styled with a blue background and white text, making it visually appealing.
// The component can be further enhanced with error handling and user feedback for a better user experience.
// The Firebase authentication functions allow for easy integration of user authentication in the application.