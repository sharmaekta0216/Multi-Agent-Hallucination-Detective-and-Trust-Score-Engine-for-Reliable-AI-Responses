// import "../styles/Navbar.css";

// function Navbar({ setPage }) {
//   return (
//     <nav className="navbar">

//       {/* Project Logo */}

//       <div className="logo">
//         Multi-Agent Hallucination Detector
//       </div>

//       {/* Navigation */}

//       <div className="nav-links">

//         <button onClick={() => setPage("home")}>
//           Home
//         </button>

//         <button onClick={() => setPage("about")}>
//           About
//         </button>

//         <button onClick={() => setPage("team")}>
//           Team
//         </button>

//         <button onClick={() => setPage("dashboard")}>
//           Dashboard
//         </button>

//       </div>

//      {/* Right Side */}

// <div className="nav-auth">

//   <button
//     className="login-nav-btn"
//     onClick={() => setPage("login")}
//   >
//     Login
//   </button>

//   <button
//     className="signup-nav-btn"
//     onClick={() => setPage("signup")}
//   >
//     Sign Up
//   </button>

// </div>

//     </nav>
//   );
// }

// export default Navbar;
// import "../Styles/Navbar.css";

// function Navbar() {
//   return (
//     <nav className="navbar">
//       <div className="logo">
//         🤖 Trust Score Engine
//       </div>

//       <ul className="nav-links">
//         <li><a href="/">Home</a></li>
//         <li><a href="/">Dashboard</a></li>
//         <li><a href="/">About</a></li>
//         <li><a href="/">Team</a></li>
//       </ul>

//       <button className="login-btn">
//         Login
//       </button>
//     </nav>
//   );
// }

// export default Navbar;
import React from "react";
import { Link } from "react-router-dom";
import "../Styles/Navbar.css";
import { FiSettings } from "react-icons/fi";

function Navbar() {
  return (
    <nav className="navbar">

      {/* Logo */}
      <div className="logo">
        🤖 Trust Score Engine
      </div>

      {/* Links */}
      <ul className="nav-links">

        <li>
          <Link to="/">Home</Link>
        </li>

        <li>
          <Link to="/dashboard">Dashboard</Link>
        </li>

        <li>
          <Link to="/charts">Charts</Link>
        </li>

        <li>
          <Link to="/team">Team</Link>
        </li>

        <li>
          <Link to="/about">About</Link>
        </li>

        <li>
          <Link to="/login">Login</Link>
        </li>

        <li>
          <Link to="/signup">Sign Up</Link>
        </li>

        <li>
          <Link to="/settings" className="settings-link">
          <FiSettings size={22} />
          </Link>
        </li>

      </ul>

    </nav>
  );
}

export default Navbar;