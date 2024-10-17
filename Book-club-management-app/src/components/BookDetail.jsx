import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';

const BookDetail = () => {
  const { id } = useParams();
  const [bookClub, setBookClub] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBookClub = async () => {
      setLoading(true);
      try {
        const response = await api.get(`/bookclubs/${id}`);
        setBookClub(response.data);
      } catch (error) {
        console.error('Error fetching book club details:', error);
        setError('Error fetching book club details. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchBookClub();
  }, [id]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h1>{bookClub.name}</h1>
      <h2>Description</h2>
      <p>{bookClub.description}</p>
      <h2>Books</h2>
      <ul>
        {bookClub.books.map((book) => (
          <li key={book.id}>
            {book.title} by {book.author}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookDetail;
