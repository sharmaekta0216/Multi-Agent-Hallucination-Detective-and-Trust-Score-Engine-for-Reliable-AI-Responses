// import "../styles/Signup.css";
// import { Link } from "react-router-dom";

// function Signup({ setPage }) {
//   return (
//     <div className="signup-page">

//       {/* Signup Card */}

//       <div className="signup-card">

//         <h1>Create Account</h1>

//         <p>
//           Join our platform to experience reliable AI responses
//           powered by multi-agent verification.
//         </p>

//         <div className="input-group">
//           <label>Full Name</label>
//           <input
//             type="text"
//             placeholder="Enter your full name"
//           />
//         </div>

//         <div className="input-group">
//           <label>Email Address</label>
//           <input
//             type="email"
//             placeholder="Enter your email"
//           />
//         </div>

//         <div className="input-group">
//           <label>Password</label>
//           <input
//             type="password"
//             placeholder="Create a password"
//           />
//         </div>

//         <button
//     className="signup-submit"
//     onClick={() => setPage("dashboard")}
// >
//     Create Account
// </button>

// <p className="login-link">
//   Already have an account?
//   <Link to="/login"> Log In</Link>
// </p>

//       </div>

//     </div>
//   );
// }

// export default Signup;
import "../Styles/Signup.css";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { FiEye, FiEyeOff } from "react-icons/fi";

function Signup() {
  const navigate = useNavigate();

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleSignup = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          full_name: fullName,
          email: email,
          password: password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Signup Successful!");
        navigate("/login");
      } else {
        alert(data.detail);
      }
    } catch (error) {
      console.error(error);
      alert("Backend connection failed.");
    }
  };

  return (
    <div className="signup-page">
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
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
          />
        </div>

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
      placeholder="Create a password"
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
          className="signup-submit"
          onClick={handleSignup}
        >
          Create Account
        </button>

        <p className="login-link">
          Already have an account?
          <Link to="/login"> Log In</Link>
        </p>

      </div>
    </div>
  );
}

export default Signup;