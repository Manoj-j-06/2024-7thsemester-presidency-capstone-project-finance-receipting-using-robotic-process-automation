import { useState, useEffect } from 'react';
import './App.css';  // For custom CSS styles
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Dashboard from './dashboard.jsx';
import Login from './login.jsx';

function App() {
    

    useEffect(() => {
        // Setting the title for the page
        document.title = 'Finance Receipting using Robotic Process Automation';
    }, []);  // Empty dependency array means this effect runs only once, when the component mounts.

    return(
        <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
    );
}

export default App;