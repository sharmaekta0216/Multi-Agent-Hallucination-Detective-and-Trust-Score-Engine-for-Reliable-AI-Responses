import "../styles/Signup.css";

function Signup({ setPage }) {
  return (
    <div className="signup-page">

      {/* Signup Card */}

      <div className="signup-card">

        <h1>Create Account</h1>

        <p>
          Join our platform to experience reliable AI responses
          powered by multi-agent verification.
        </p>

        <div className="input-group">
          <label>Full Name</label>
          <input
            type="text"
            placeholder="Enter your full name"
          />
        </div>

        <div className="input-group">
          <label>Email Address</label>
          <input
            type="email"
            placeholder="Enter your email"
          />
        </div>

        <div className="input-group">
          <label>Password</label>
          <input
            type="password"
            placeholder="Create a password"
          />
        </div>

        <button
    className="signup-submit"
    onClick={() => setPage("dashboard")}
>
    Create Account
</button>

      </div>

    </div>
  );
}

export default Signup;