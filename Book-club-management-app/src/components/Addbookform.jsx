import React, { useState } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';

const AddBookForm = ({ clubId }) => {
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const initialValues = {
    title: '',
    author: '',
  };

  const validationSchema = Yup.object().shape({
    title: Yup.string().required('Required'),
    author: Yup.string().required('Required'),
  });

  const handleSubmit = async (values, { setSubmitting }) => {
    try {
      const response = await axios.post(`/api/book-clubs/${clubId}/books`, values);
      setSuccessMessage('Book added successfully!');
      setSubmitting(false);
    } catch (error) {
      setErrorMessage('Error adding book. Please try again.');
      setSubmitting(false);
    }
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      {({ isSubmitting }) => (
        <Form>
          <div>
            <label htmlFor="title">Title:</label>
            <Field type="text" id="title" name="title" />
            <ErrorMessage name="title" component="div" />
          </div>
          <div>
            <label htmlFor="author">Author:</label>
            <Field type="text" id="author" name="author" />
            <ErrorMessage name="author" component="div" />
          </div>
          <button type="submit" disabled={isSubmitting}>
            Add Book
          </button>
          {successMessage && <p className="success">{successMessage}</p>}
          {errorMessage && <p className="error">{errorMessage}</p>}
        </Form>
      )}
    </Formik>
  );
};

export default AddBookForm;
