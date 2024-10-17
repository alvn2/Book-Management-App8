import React from 'react';
const Home = () => {
  return (
    <div className="home">
      <h1>Building Community Through Books</h1>
      <p>Organize your club, start a new one, or find your book people.</p>
      <button className="cta-button">Start a Club</button>
      <div className="features">
        <h2>Get Your Club Organized</h2>
        <p>Create a book club or add your existing club — it’s easy!</p>
      </div>
      <div className="features">
        <h2>Find Your Book People</h2>
        <p>Discover clubs that align with your reading interests.</p>
        </div>
        <div className="features">
          <h2>Share Your Love of Reading</h2>
          <p>Connect with fellow book lovers and make new friends.</p>
        </div>
      </div>
  );
}; 
export default Home;