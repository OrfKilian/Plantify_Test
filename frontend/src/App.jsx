import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/api/ping`)
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage('Fehler beim Laden der API'));
  }, []);

  return (
    <div>
      <h1>Plantify Frontend</h1>
      <p>Antwort der API: {message}</p>
    </div>
  );
}

export default App;
