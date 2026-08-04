import { Link, useNavigate } from "react-router-dom";
import "../Styles/SettingsDropdown.css";

function SettingsDropdown({ onClose }) {

  const navigate = useNavigate();

  const handleLogout = () => {

    // Clear logged-in user
    localStorage.removeItem("user_id");
    localStorage.removeItem("name");
    localStorage.removeItem("email");

    // Close dropdown
    onClose();

    // Redirect to Home
    navigate("/");

    // Refresh components
    window.location.reload();
  };

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

      <button
        className="dropdown-item logout"
        onClick={handleLogout}
      >
        🚪 Logout
      </button>

    </div>

  );
}

export default SettingsDropdown;