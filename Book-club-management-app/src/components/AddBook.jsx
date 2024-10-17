import React from 'react';
import { useParams } from 'react-router-dom';
import BookForm from './BookForm'; 

const AddBook = () => {
  const { clubId } = useParams(); 

  return (
    <div>
      <h2>Add a New Book</h2>
      <BookForm clubId={clubId} /> {/* Pass the clubId to BookForm */}
    </div>
  );
};

export default AddBook;