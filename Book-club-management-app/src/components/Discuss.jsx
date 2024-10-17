import React, { useState } from 'react';

const Discuss = () => {
  const [discussions, setDiscussions] = useState([]);
  const [newDiscussion, setNewDiscussion] = useState('');

  const handleAddDiscussion = (e) => {
    e.preventDefault();
    if (newDiscussion.trim()) {
      setDiscussions([...discussions, newDiscussion]);
      setNewDiscussion(''); // Clear the input
    }
  };

  return (
    <div>
      <h2>Discussions</h2>
      
      <form onSubmit={handleAddDiscussion}>
        <input
          type="text"
          value={newDiscussion}
          onChange={(e) => setNewDiscussion(e.target.value)}
          placeholder="Share your thoughts..."
          required
        />
        <button type="submit">Add Discussion</button>
      </form>
      
      <ul>
        {discussions.map((discussion, index) => (
          <li key={index}>{discussion}</li>
        ))}
      </ul>
    </div>
  );
};

export default Discuss;
