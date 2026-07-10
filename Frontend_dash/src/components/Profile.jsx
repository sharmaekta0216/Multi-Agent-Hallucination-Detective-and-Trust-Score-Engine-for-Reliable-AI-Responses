import "../Styles/Profile.css";

function Profile() {
  return (

    <div className="profile-page">

      <div className="profile-card">

        <h1>👤 Profile</h1>

        <p><strong>Name:</strong> User Name</p>

        <p><strong>Email:</strong> user@email.com</p>

        <p className="profile-note">
          Profile information will be loaded from the database after login.
        </p>

      </div>

    </div>

  );
}

export default Profile;