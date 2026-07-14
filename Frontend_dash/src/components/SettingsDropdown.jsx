import { Link } from "react-router-dom";
import "../Styles/SettingsDropdown.css";

function SettingsDropdown({ onClose }) {
  return (
    <div className="settings-dropdown">

      <Link
        to="/profile"
        className="dropdown-item"
        onClick={onClose}
      >
        👤 Profile
      </Link>

      <Link
        to="/history"
        className="dropdown-item"
        onClick={onClose}
      >
        🕒 History
      </Link>

      <div className="dropdown-divider"></div>

      <Link
        to="/"
        className="dropdown-item logout"
        onClick={onClose}
      >
        🚪 Logout
      </Link>

    </div>
  );
}

export default SettingsDropdown;