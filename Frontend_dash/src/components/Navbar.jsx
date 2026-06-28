function Navbar({ setPage }) {
  return (
    <nav className="navbar">

      {/* Project Logo */}

      <div className="logo">
        Multi-Agent Hallucination Detector
      </div>

      {/* Navigation */}

      <div className="nav-links">

        <button onClick={() => setPage("home")}>
          Home
        </button>

        <button onClick={() => setPage("about")}>
          About
        </button>

        <button onClick={() => setPage("team")}>
          Team
        </button>

        <button onClick={() => setPage("dashboard")}>
          Dashboard
        </button>

      </div>

     {/* Right Side */}

<div className="nav-auth">

  <button
    className="login-nav-btn"
    onClick={() => setPage("login")}
  >
    Login
  </button>

  <button
    className="signup-nav-btn"
    onClick={() => setPage("signup")}
  >
    Sign Up
  </button>

</div>

    </nav>
  );
}

export default Navbar;