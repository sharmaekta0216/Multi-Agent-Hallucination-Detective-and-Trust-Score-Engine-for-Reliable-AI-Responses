/*import "../Styles/Settings.css";

function Settings() {
  return (
    <div className="settings-container">

      <h1>⚙ Settings</h1>

      <p>
        Customize your experience with the Trust Score Engine.
      </p>

      <div className="settings-card">

        <div className="setting-item">
          <label>
            <input type="checkbox" />
            Dark Mode
          </label>
        </div>

        <div className="setting-item">
          <label>
            <input type="checkbox" />
            Show Trust Score Details
          </label>
        </div>

        <div className="setting-item">
          <label>
            <input type="checkbox" />
            Save Chat History
          </label>
        </div>

        <div className="setting-item">
          <label>
            <input type="checkbox" />
            Enable Notifications
          </label>
        </div>

      </div>

    </div>
  );
}

export default Settings;*/

import "../Styles/Settings.css";
import { Link, useNavigate } from "react-router-dom";

function Settings() {

  const navigate = useNavigate();

  const handleLogout = () => {
    // Later we'll remove the login session here.
    navigate("/");
  };

  return (
    <div className="settings-page">

      <div className="settings-card">

        <h1>⚙ Settings</h1>

        <p className="settings-subtitle">
          Manage your account and application preferences.
        </p>

        <Link to="/profile" className="setting-box">
          👤 Profile
        </Link>

        <Link to="/history" className="setting-box">
          🕒 History
        </Link>

        <button
          className="logout-btn"
          onClick={handleLogout}
        >
          🚪 Log Out
        </button>

      </div>

    </div>
  );
}

export default Settings;