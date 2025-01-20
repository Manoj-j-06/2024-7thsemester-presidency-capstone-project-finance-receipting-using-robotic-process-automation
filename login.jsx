import React from 'react';
import './Dashboard.css'; // Optional for styling
import { useNavigate } from 'react-router-dom';  // Correct hook for React Router v6
import { useState } from 'react';
import './login.css'; // Optional for styling

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();  // Initialize useNavigate hook

    // Handle form submission
    const handleSubmit = (e) => {
            e.preventDefault();
            if (username === 'admin' && password === 'password') {
                navigate('/dashboard');
            } else {
                alert('Invalid username or password');
            }
        };

    return (
        <div className="login-container">
            <div>
                <h2>Finance Receipting using Robotic Process Automation</h2>
                <p>Automating financial receipt processing using RPA technology.</p>
            </div>
            <div className="login-card">
                <form onSubmit={handleSubmit}>
                    <div className="input-group">
                        <label htmlFor="username">Username</label>
                        <input
                            type="text"
                            id="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Enter username"
                            required
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Enter password"
                            required
                        />
                    </div>
                    <button type="submit">Login</button>
                </form>
            </div>
        </div>
    );
};

export default Login;
