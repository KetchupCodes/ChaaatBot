import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
const formatNewlines = (text) => {
  return text.split('\n').map((line, index) => (
    <React.Fragment key={index}>
      {line}
      <br />
    </React.Fragment>
  ));
};
function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:5000/chatbot', { message });
      setResponse(res.data.response);
      // Process the response and display images
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="App">
      <h1>Chaatbot</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message"
        />
        <button type="submit">Send</button>
      </form>
      <div>
        <p>{formatNewlines(response)}</p>
      </div>
    </div>
  );
}

export default App;
