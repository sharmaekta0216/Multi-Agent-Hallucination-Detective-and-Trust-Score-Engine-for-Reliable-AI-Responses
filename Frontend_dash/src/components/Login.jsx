/*import "../styles/Login.css";

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

export default Login;*/

import "../Styles/Login.css";
import { Link, useNavigate } from "react-router-dom";

function Login() {

  const navigate = useNavigate();

  return (
    <div className="login-page">

      <div className="login-card">

        <h1>Sign In</h1>

        <p className="login-subtitle">
          Welcome back! Log In to continue.
        </p>

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
          onClick={() => navigate("/dashboard")}
        >
          Login
        </button>

        <p className="signup-link">
          Don't have an account?
          <Link to="/signup"> Sign Up</Link>
        </p>

      </div>

    </div>
  );
}

export default Login;