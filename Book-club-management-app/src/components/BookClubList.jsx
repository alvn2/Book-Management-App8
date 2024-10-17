import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const BookClubList = () => {
  const [bookClubs, setBookClubs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBookClubs = async () => {
      try {
        const response = await axios.get('/api/bookclubs'); // Replace with the correct API route
        setBookClubs(response.data);
      } catch (error) {
        setError('Error fetching book clubs. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchBookClubs();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h2>Available Book Clubs</h2>
      <ul>
        {bookClubs.map((club) => (
          <li key={club.id}>
            <Link to={`/book-clubs/${club.id}`}>{club.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookClubList;
