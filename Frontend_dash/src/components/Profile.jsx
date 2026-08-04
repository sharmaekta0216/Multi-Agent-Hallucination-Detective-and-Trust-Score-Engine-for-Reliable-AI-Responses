import "../Styles/Profile.css";

function Profile() {

  const name = localStorage.getItem("name") || "User";
  const email = localStorage.getItem("email") || "Please Login";

  const initials =
    name === "User"
      ? "U"
      : name
          .split(" ")
          .map((word) => word[0])
          .join("")
          .toUpperCase();

  return (
    <div className="profile-page">

      <div className="profile-card">

        <div className="profile-avatar">
          {initials}
        </div>

        <h2 className="profile-name">
          {name}
        </h2>

        <p className="profile-email">
          {email}
        </p>

        {name === "User" && (
          <button
            className="profile-login-btn"
            onClick={() => window.location.href = "/login"}
          >
            Login
          </button>
        )}

      </div>

    </div>
  );
}

export default Profile;