/* import { useState } from 'react';
import axios from 'axios';
import InputField from '../../components/InputField/InputField';
import Button from '../../components/Button/Button';
import '../Register/RegisterStyles.css';

function Register() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      alert('As senhas não correspondem.');
      return;
    }

    const userData = {
      username: name, // O backend espera "username", então usamos esse campo
      email: email,
      password: password,
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/usuario/register/', userData);
      console.log('Usuário cadastrado com sucesso:', response.data);
      alert('Cadastro realizado com sucesso!');
    } catch (error) {
      if (error.response) {
        console.error('Erro ao cadastrar usuário:', error.response.data);
        alert('Erro ao cadastrar usuário: ' + error.response.data.detail || 'Verifique os dados.');
      } else {
        console.error('Erro de rede:', error);
        alert('Erro de rede ao tentar cadastrar usuário.');
      }
    }
  };

  return (
    <div className="container">
      <h1 className="title has-text-centered">Cadastro de Usuário</h1>
      <form onSubmit={handleSubmit} className="box">
        <div className="field">
          <label className="label">Nome</label>
          <div className="control">
            <InputField
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Nome"
              required
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Email</label>
          <div className="control">
            <InputField
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Email"
              required
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Senha</label>
          <div className="control">
            <InputField
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Senha"
              required
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Confirmar Senha</label>
          <div className="control">
            <InputField
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirme sua senha"
              required
            />
          </div>
        </div>

        <div className="field">
          <div className="control">
            <Button type="submit">Cadastrar</Button>
          </div>
        </div>
      </form>
    </div>
  );
}

export default Register;
 */

import { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Para redirecionar após cadastro
import axios from 'axios';
import InputField from '../../components/InputField/InputField';
import Button from '../../components/Button/Button';
import './RegisterStyles.css';
import Navbar from '../../components/Navbar/NavBar';

function Register() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const navigate = useNavigate(); // Hook para navegação

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      alert('As senhas não correspondem.');
      return;
    }

    const userData = {
      username: name,
      email,
      password,
    };

    try {
      await axios.post('http://127.0.0.1:8000/usuario/register/', userData);
      alert('Cadastro realizado com sucesso!');
      navigate('/login'); // Redireciona para a página de login
    } catch (error) {
      if (error.response) {
        alert('Erro ao cadastrar usuário: ' + (error.response.data.detail || 'Verifique os dados.'));
      } else {
        alert('Erro de rede ao tentar cadastrar usuário.');
      }
    }
  };

  return (
    <div className="container">
      <Navbar/>
      <h1 className="title has-text-centered">Cadastro de Usuário</h1>
      <form onSubmit={handleSubmit} className="box">
        <div className="field">
          <label className="label">Nome</label>
          <InputField
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Nome"
            required
          />
        </div>

        <div className="field">
          <label className="label">Email</label>
          <InputField
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            required
          />
        </div>

        <div className="field">
          <label className="label">Senha</label>
          <InputField
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Senha"
            required
          />
        </div>

        <div className="field">
          <label className="label">Confirmar Senha</label>
          <InputField
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            placeholder="Confirme sua senha"
            required
          />
        </div>

        <div className="field">
          <Button type="submit">Cadastrar</Button>
        </div>
      </form>
    </div>
  );
}

export default Register;
