/* import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Fazendo a requisição GET para a API do Django
    axios.get('http://127.0.0.1:8000/example/')
      .then(response => {
        // Salvando a mensagem no estado
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error('Erro ao buscar a mensagem:', error);
      });
  }, []);

  return (
    <div>
      <h1>React + Django</h1>
      <p>Mensagem do Django: {message}</p>
    </div>
  );
}

export default App; */

import Login from './pages/Login/Login';

const App = () => {
  return (
    <div className="App">
      <Login />
    </div>
  );
};

export default App;

