import "../Styles/Settings.css";

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

export default Settings;