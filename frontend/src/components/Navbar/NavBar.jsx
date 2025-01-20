import { Link  } from 'react-router-dom';

function Navbar(){
    
    return(
        
        <nav style={navbarStyles.navbar}>
            <div style={navbarStyles.navContent}>
                <h1 style={navbarStyles.title}>Minha Aplicação</h1>
                
                <div>
                    <Link to="/" style={navbarStyles.link}>
                        Login
                    </Link>
                    <Link to="/register" style={navbarStyles.link}>
                        Registrar
                    </Link>
                </div>
            </div>
        </nav>
    )
}


export default Navbar


// Estilos para a Navbar
const navbarStyles = {
    navbar: {
      position: 'fixed',
      top: 0,
      left: 0,
      width: '100%',
      backgroundColor: '#000',
      color: '#fff',
      padding: '1rem 2rem',
      boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
      zIndex: 1000,
    },
    navContent: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      maxWidth: '1200px',
      margin: '0 auto',
    },
    title: {
      fontSize: '1.5rem',
      fontWeight: 'bold',
    },
    buttonContainer: {
      display: 'flex',
      gap: '1rem',
    },
    button: {
      backgroundColor: '#1877f2',
      color: '#fff',
      border: 'none',
      borderRadius: '4px',
      padding: '0.5rem 1rem',
      fontSize: '1rem',
      cursor: 'pointer',
      transition: 'background-color 0.3s',
    },
    buttonHover: {
      backgroundColor: '#145db2',
    },
    link: {
      color: '#fff',
      margin: '0 1rem',
      textDecoration: 'none',
      fontSize: '1rem',
    },
  };
  