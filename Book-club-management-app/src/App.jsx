import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import CreateBookClubForm from './components/CreateBookClubForm';
import JoinBookClub from './components/JoinBookClub';
import Discuss from './components/Discuss';
import BookClubList from './components/BookClubList';
import BookDetail from './components/BookDetail';
import AddBookForm from './components/AddBookForm';
import SubmitReviewForm from './components/SubmitReviewForm';

const App = () => {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/create-bookclub" element={<CreateBookClubForm />} />
            <Route path="/join-bookclub" element={<JoinBookClub />} />
            <Route path="/discuss" element={<Discuss />} />
            <Route path="/bookclubs" element={<BookClubList />} />
            <Route path="/bookclubs/:id" element={<BookDetail />} />
            <Route path="/bookclubs/:clubId/add-book" element={<AddBookForm />} />
            <Route path="/bookclubs/:clubId/books/:bookId/review" element={<SubmitReviewForm />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
