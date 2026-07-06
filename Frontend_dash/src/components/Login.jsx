import "../styles/Login.css";

function Login({ setPage }) {
  return (
    <div className="login-page">

      <div className="login-card">

        <h1>Sign In</h1>

        <p>Welcome back! Sign in to continue.</p>

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
            placeholder="Enter your password"
          />

        </div>

        <button
          className="login-btn"
          onClick={() => setPage("dashboard")}
        >
          Login
        </button>

      </div>

    </div>
  );
}

export default Login;