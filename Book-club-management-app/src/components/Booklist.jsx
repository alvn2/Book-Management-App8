import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const BookList = () => {
  const { clubId } = useParams(); // Get clubId from the URL
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const response = await axios.get(`/api/bookclubs/${clubId}/books`); // Adjust API endpoint as necessary
        setBooks(response.data); // Assuming the response is an array of books
      } catch (err) {
        setError('Error fetching books. Please try again.');
      } finally {
        setLoading(false);
      }
    };

    fetchBooks();
  }, [clubId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h2>Books</h2>
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            {book.title} by {book.author}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookList;
