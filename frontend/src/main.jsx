/* import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Register from './pages/Register/Register.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'


const router = createBrowserRouter([
  {
    path: "/login",
    element: <App />
  },
  {
    path: "/register",
    element: <Register/>
  }
]);
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
 */

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App.jsx';
import Register from './pages/Register/Register.jsx';
import Login from './pages/Login/Login.jsx'; // Importa a página de login
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

// Configuração das rotas
const router = createBrowserRouter([
  {
    path: "/login",
    element: <Login /> // Define Login na rota /login
  },
  {
    path: "/register",
    element: <Register /> // Define Register na rota /register
  },
  {
    path: "/",
    element: <App /> // Define App como rota principal
  },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
