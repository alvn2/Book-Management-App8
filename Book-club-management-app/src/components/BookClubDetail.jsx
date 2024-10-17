import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const BookClubDetail = () => {
  const { id } = useParams();
  const [bookClub, setBookClub] = useState(null);
  const [loading, setLoading] = useState(true); // State to manage loading status
  const [error, setError] = useState(null); // State to handle errors

  useEffect(() => {
    const fetchBookClub = async () => {
      try {
        const response = await fetch(`/api/bookclubs/${id}`); // Replace with the correct API route
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setBookClub(data);
      } catch (error) {
        setError(error.message); // Set error message
      } finally {
        setLoading(false); // Update loading state
      }
    };

    fetchBookClub();
  }, [id]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>; // Display error message

  return (
    <div>
      <h2>{bookClub.name}</h2>
      <p>{bookClub.description}</p>
      <h3>Books</h3>
      <ul>
        {bookClub.books.map((book) => (
          <li key={book.id}>{book.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default BookClubDetail;
