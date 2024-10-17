import React, { useState } from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom'; 

const SubmitReviewForm = () => {
  const { clubId, bookId } = useParams(); 
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();   

  const initialValues = {
    rating: '',
    comment: '',
  };   

  const validationSchema = Yup.object().shape({
    rating: Yup.number().required('Required').min(1).max(5),
    comment: Yup.string().required('Required'),
  });   

  const handleSubmit = async (values, { setSubmitting }) => {
    try {
      await axios.post(`/api/book-clubs/${clubId}/books/${bookId}/reviews`, values);
      setSuccessMessage('Review submitted successfully!');
      setSubmitting(false);
      navigate(`/book-clubs/${clubId}/books`); 
    } catch (error) {
      setErrorMessage('Error submitting review. Please try again.');
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
            <label htmlFor="rating">Rating (1-5):</label>
            <Field type="number" id="rating" name="rating" />
            <ErrorMessage name="rating" component="div" />
          </div>
          <div>
            <label htmlFor="comment">Comment:</label>
            <Field as="textarea" id="comment" name="comment" />
            <ErrorMessage name="comment" component="div" />
          </div>
          <button type="submit" disabled={isSubmitting}>
            Submit Review
          </button>
          {successMessage && <p className="success">{successMessage}</p>}
          {errorMessage && <p className="error">{errorMessage}</p>}
        </Form>
      )}
    </Formik>
  );
}; 

export default SubmitReviewForm;
