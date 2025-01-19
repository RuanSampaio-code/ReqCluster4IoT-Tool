import { useState } from 'react';
/* import 'bulma/css/bulma.min.css'; // Importa o Bulma CSS */

import InputField from '../../components/InputField/InputField';
import Button from '../../components/Button/Button';
/* import '../../pages/';  */// Importando o CSS


function Register() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      alert('As senhas não correspondem.');
      return;
    }

    // Aqui você pode enviar os dados para a API
    console.log('Usuário cadastrado:', { name, email, password });
    alert('Cadastro realizado com sucesso!');
  };

  return (
    <div className="container is-fluid">
      <div className="section">
        <h1 className="title has-text-centered">Cadastro de Usuário</h1>
        <form onSubmit={handleSubmit} className="box">
          <div className="field">
            <label className="label">Nome</label>
            <div className="control">
              <InputField
                type="Nome"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Nome"
                
              />
            </div>
          </div>

          <div className="field">
            <label className="label">Email</label>
            <div className="control">
            <InputField
                type="Nome"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
                
              />
            </div>
          </div>

          <div className="field">
            <label className="label">Senha</label>
            <div className="control">
              <InputField
                type=  'password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Senha"
              
              />
            </div>
          </div>

          <div className="field">
            <label className="label">Confirmar Senha</label>
            <div className="control">
              <InputField
                className="input"
                type="password"
                placeholder="Confirme sua senha"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
              />
            </div>
          </div>

          <div className="field">
            <div className="control">
              <Button type="submit" >
              Entrar
              </Button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Register;

