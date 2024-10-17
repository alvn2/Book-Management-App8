import React, { useEffect, useState } from 'react';
import axios from 'axios';

const JoinBookClub = () => {
  const [bookClubs, setBookClubs] = useState([]);

  useEffect(() => {
    const fetchBookClubs = async () => {
      try {
        const response = await axios.get('/api/book-clubs'); // Adjust this endpoint as needed
        setBookClubs(response.data);
      } catch (error) {
        console.error('Error fetching book clubs:', error);
      }
    };

    fetchBookClubs();
  }, []);

  return (
    <div>
      <h2>Join a Book Club</h2>
      {bookClubs.length > 0 ? (
        <ul>
          {bookClubs.map((club) => (
            <li key={club.id}>
              <h3>{club.name}</h3>
              <p>{club.description}</p>
              <button onClick={() => alert(`Joined ${club.name}`)}>Join</button>
            </li>
          ))}
        </ul>
      ) : (
        <p>No book clubs available to join.</p>
      )}
    </div>
  );
};

export { JoinBookClub };
