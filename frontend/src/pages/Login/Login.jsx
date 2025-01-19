import { useState, useEffect } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import InputField from '../../components/InputField/InputField';
import Button from '../../components/Button/Button';
import styles from './LoginForm.module.css';
import Navbar from '../../components/Navbar/NavBar';

const LoginForm = () => {

  
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');


  useEffect(() => {
    validateEmail(email);
    validatePassword(password);
  }, [email, password]);

  const validateEmail = (value) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    setEmailError(value && !emailRegex.test(value) ? 'E-mail inválido' : '');
  };

  const validatePassword = (value) => {
    setPasswordError(value.length < 3 ? 'A senha deve ter pelo menos 3 caracteres' : '');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!emailError && !passwordError && email && password) {
      toast.success('Login realizado com sucesso!');
    } else {
      toast.error('Por favor, corrija os erros no formulário.');
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div>
      {/* Navbar */}
     
      <Navbar />
      {/* Formulário de Login */}
      <div className={styles.loginContainer}>
        <form onSubmit={handleSubmit} className={styles.loginForm}>
          <h2 className={styles.title}>Login</h2>
          <InputField
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="E-mail"
            error={emailError}
          />
          <InputField
            type={showPassword ? 'text' : 'password'}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Senha"
            error={passwordError}
            togglePassword={togglePasswordVisibility}
            showPassword={showPassword}
          />
          <Button type="submit" disabled={!!emailError || !!passwordError || !email || !password}>
            Entrar
          </Button>
          <a href="#" className={styles.forgotPassword}>Esqueci minha senha</a>
        </form>
        <ToastContainer position="bottom-right" />
      </div>
    </div>
  );
};

// Estilos para a Navbar

export default LoginForm;
