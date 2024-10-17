import React, { useState } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const CreateBookClubForm = () => {
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate(); // Initialize navigate

  const initialValues = {
    name: '',
    description: '',
  };

  const validationSchema = Yup.object().shape({
    name: Yup.string().required('Required'),
    description: Yup.string().required('Required'),
  });

  const handleSubmit = async (values, { setSubmitting }) => {
    try {
      const response = await axios.post('/api/book-clubs', values);
      setSuccessMessage('Book club created successfully!');
      setSubmitting(false);
      navigate('/book-clubs'); // Navigate to book clubs page
    } catch (error) {
      setErrorMessage('Error creating book club. Please try again.');
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
            <label htmlFor="name">Name:</label>
            <Field type="text" id="name" name="name" />
            <ErrorMessage name="name" component="div" />
          </div>
          <div>
            <label htmlFor="description">Description:</label>
            <Field as="textarea" id="description" name="description" />
            <ErrorMessage name="description" component="div" />
          </div>
          <button type="submit" disabled={isSubmitting}>
            Create Book Club
          </button>
          {successMessage && <p className="success">{successMessage}</p>}
          {errorMessage && <p className="error">{errorMessage}</p>}
        </Form>
      )}
    </Formik>
  );
};

export default CreateBookClubForm;
