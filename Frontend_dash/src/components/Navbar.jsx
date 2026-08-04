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
// 
import React, { useState, useEffect, useRef } from "react";
import { NavLink } from "react-router-dom";
import "../Styles/Navbar.css";
import { FiSettings } from "react-icons/fi";
import SettingsDropdown from "./SettingsDropdown";

function Navbar() {
  const [showSettings, setShowSettings] = useState(false);
  const dropdownRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target)
      ) {
        setShowSettings(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <>
      <nav className="navbar">
        {/* Logo */}
        <div className="logo">
          🤖 Trust Score Engine
        </div>

        {/* Navigation Links */}
        <ul className="nav-links">

          <li>
            <NavLink to="/">Home</NavLink>
          </li>

          <li>
            <NavLink to="/dashboard">Dashboard</NavLink>
          </li>

          <li>
            <NavLink to="/team">Team</NavLink>
          </li>

          <li>
            <NavLink to="/about">About</NavLink>
          </li>

          <li>
            <NavLink to="/login">Login</NavLink>
          </li>

          <li>
            <NavLink to="/signup">Sign Up</NavLink>
          </li>

          <li className="settings-wrapper">
            <button
              className="settings-btn"
              onClick={() => setShowSettings(!showSettings)}
            >
              <FiSettings size={22} />
            </button>
          </li>

        </ul>
      </nav>

      {showSettings && (
        <div ref={dropdownRef}>
          <SettingsDropdown
            onClose={() => setShowSettings(false)}
          />
        </div>
      )}
    </>
  );
}

export default Navbar;