import "../Styles/Login.css";
import { useState } from "react";
import { Link } from "react-router-dom";
import { FiEye, FiEyeOff } from "react-icons/fi";


function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = async () => {

    if (!email.trim() || !password.trim()) {
    alert("Please enter your email and password.");
    return;
  }

    try {

      const response = await fetch("http://127.0.0.1:8000/login", {

        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({

          email: email,
          password: password,

        }),

      });

      const data = await response.json();

      if (response.ok) {

        localStorage.setItem("user_id", data.user_id);
        localStorage.setItem("name", data.name);
        localStorage.setItem("email", data.email);

        alert("Login Successful!");

        window.location.href = "/dashboard";

      } else {

        alert(data.detail);

      }

    } catch (error) {

      console.error(error);

      alert("Backend connection failed.");

    }

  };

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
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

        </div>

        <div className="input-group">

          <label>Password</label>

          <div className="password-field">

            <input
              type={showPassword ? "text" : "password"}
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <span
              className="eye-icon"
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? <FiEyeOff /> : <FiEye />}
            </span>

          </div>

        </div>

        <button
          className="login-btn"
          onClick={handleLogin}
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
