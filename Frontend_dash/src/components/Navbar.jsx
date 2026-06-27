function Navbar({ setPage }) {
  return (
    <nav className="navbar">

      <div className="logo">
        Trust Score Engine
      </div>

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

      </div>

      <button
        className="signup-nav-btn"
        onClick={() => setPage("signup")}
      >
        Sign Up
      </button>

    </nav>
  );
}

export default Navbar;