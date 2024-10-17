import axios from 'axios';

// Create an Axios instance with the base URL of the Flask API
const api = axios.create({
  baseURL: 'http://localhost:5000/api', // Adjust with your Flask server URL
});

export default api;
