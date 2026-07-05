import "../Styles/Footer.css";

function Footer() {
  return (
    <footer className="footer">

      <div className="footer-container">

        <div className="footer-left">
          <h2>🤖 Trust Score Engine</h2>

          <p>
            Multi-Agent Hallucination Detection &
            Trust Score Engine for Reliable AI Responses.
          </p>
        </div>

        <div className="footer-center">
          <h3>Quick Links</h3>

          <p>Home</p>
          <p>Dashboard</p>
          <p>About</p>
          <p>Team</p>
        </div>

        <div className="footer-right">
          <h3>Technology</h3>

          <p>React</p>
          <p>FastAPI</p>
          <p>Python</p>
          <p>MySQL</p>
        </div>

      </div>

      <hr />

      <p className="copyright">
        © 2026 Trust Score Engine | Developed by Team
      </p>

    </footer>
  );
}

export default Footer;