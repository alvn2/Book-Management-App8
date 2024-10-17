import * as Yup from 'yup';

// Validation schema for BookForm
export const bookFormValidation = Yup.object({
  title: Yup.string().required('Title is required'),
  author: Yup.string().required('Author is required'),
  yearPublished: Yup.number()
    .required('Year is required')
    .min(1800, 'Year must be after 1800')
    .max(new Date().getFullYear(), `Year can't be in the future`),
});

// Validation schema for ReviewForm
export const reviewFormValidation = Yup.object({
  rating: Yup.number()
    .required('Rating is required')
    .min(1, 'Rating must be at least 1')
    .max(5, 'Rating can’t be more than 5'),
  comment: Yup.string().required('Comment is required'),
});
