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
import axios from 'axios';
import { useState, useEffect } from 'react';


/* const App = () => {

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/auth/');
      setData(response.data);
    } catch (error) {
      console.error('Erro ao obter os dados:', error);
    }
  };

  return (
    <div className="App">
      <Login />
    </div>
  );
};
 */

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/auth/') // URL do backend Django
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error('Erro ao buscar a mensagem:', error);
      });
  }, []);

  return (
    
    <div>

      <nav style={{ backgroundColor: '#333', padding: '1rem', color: '#fff' }}>
        <div style={{ display: 'flex', justifyContent: 'space-around', alignItems: 'center' }}>
          <h1>React + Django</h1>
          <div>
            <a href="#login" style={{ color: '#fff', margin: '0 1rem', textDecoration: 'none' }}>Login</a>
            <a href="#register" style={{ color: '#fff', margin: '0 1rem', textDecoration: 'none' }}>Registrar</a>
          </div>
        </div>
      </nav>
      <h1>React + Django</h1>
      <p>Mensagem do Django: {message}</p>

      <div className="App">
      <Login />
    </div>
    </div>
  );
}

export default App;

