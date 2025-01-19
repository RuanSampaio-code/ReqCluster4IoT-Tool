import PropTypes from 'prop-types'; // Importação de PropTypes
import { Eye, EyeOff } from 'lucide-react';
import styles from './Input.module.css';

const InputField = ({
  type,
  value,
  onChange,
  placeholder,
  error,
  togglePassword,
  showPassword,
}) => {
  const isPasswordField = type === 'password';

  return (
    <div className={styles.inputContainer}>
      <input
        type={isPasswordField && showPassword ? 'text' : type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className={`${styles.input} ${error ? styles.inputError : ''}`}
      />
      {isPasswordField && togglePassword && (
        <button type="button" onClick={togglePassword} className={styles.togglePassword}>
          {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
        </button>
      )}
      {error && <span className={styles.errorMessage}>{error}</span>}
    </div>
  );
};

// PropTypes para validação de props
InputField.propTypes = {
  type: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  placeholder: PropTypes.string,
  error: PropTypes.string,
  togglePassword: PropTypes.func,
  showPassword: PropTypes.bool,
};

InputField.defaultProps = {
  placeholder: '',
  error: '',
  togglePassword: null,
  showPassword: false,
};

export default InputField;
