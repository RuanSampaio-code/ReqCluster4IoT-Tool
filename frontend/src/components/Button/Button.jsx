import PropTypes from 'prop-types';
import styles from './Button.module.css';

const Button = ({ children, ...props }) => {
  return (
    <button className={styles.button} {...props}>
      {children}
    </button>
  );
};

Button.propTypes = {
  children: PropTypes.node.isRequired, // Especifica que 'children' é obrigatório
};

export default Button;