import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import api from '../services/api'; 

const BookForm = ({ clubId }) => {
  
  const validationSchema = Yup.object({
    title: Yup.string().required('Title is required'),
    author: Yup.string().required('Author is required'),
    yearPublished: Yup.number()
      .required('Year is required')
      .min(1800, 'Year must be after 1800')
      .max(new Date().getFullYear(), `Year can't be in the future`),
  });

  const handleSubmit = async (values, { setSubmitting, resetForm }) => {
    try {
      
      await api.post(`/bookclubs/${clubId}/books`, values);
      alert('Book added successfully!');
      resetForm(); 
    } catch (error) {
      console.error('Error adding book:', error);
      alert('Failed to add the book. Please try again.');
    } finally {
      setSubmitting(false); 
    }
  };

  return (
    <Formik
      initialValues={{ title: '', author: '', yearPublished: '' }}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      {({ isSubmitting }) => (
        <Form>
          <div>
            <label htmlFor="title">Title</label>
            <Field type="text" name="title" />
            <ErrorMessage name="title" component="div" />
          </div>

          <div>
            <label htmlFor="author">Author</label>
            <Field type="text" name="author" />
            <ErrorMessage name="author" component="div" />
          </div>

          <div>
            <label htmlFor="yearPublished">Year Published</label>
            <Field type="number" name="yearPublished" />
            <ErrorMessage name="yearPublished" component="div" />
          </div>

          <button type="submit" disabled={isSubmitting}>
            Add Book
          </button>
        </Form>
      )}
    </Formik>
  );
};

export default BookForm;
