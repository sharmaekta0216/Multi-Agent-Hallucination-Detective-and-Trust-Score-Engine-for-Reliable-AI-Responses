import "../Styles/Profile.css";

function Profile() {

  const name = localStorage.getItem("name") || "Guest";

  const email = localStorage.getItem("email") || "Not Available";

  const initials = name
    .split(" ")
    .map(word => word[0])
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

      </div>

    </div>

  );

}

export default Profile;