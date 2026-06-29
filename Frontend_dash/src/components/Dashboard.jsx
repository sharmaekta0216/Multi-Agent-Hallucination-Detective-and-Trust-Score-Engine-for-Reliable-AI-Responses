import { useState } from "react";
import "../styles/Dashboard.css";

function Dashboard() {

  const [question, setQuestion] = useState("");

  return (

    <div className="dashboard">

      <h1>AI Verification Dashboard</h1>

      <p className="dashboard-subtitle">
        Ask a question and let our multi-agent system verify the response before
        generating a Trust Score.
      </p>

      <div className="dashboard-grid">

        {/* LEFT SIDE */}

        <div className="question-card">

          <h2>Ask Your Question</h2>

          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Example: What is Artificial Intelligence?"
          />

          <button className="analyze-btn">
            Analyze Response
          </button>

        </div>

        {/* RIGHT SIDE */}

        <div className="summary-card">

          <h2>Analysis Summary</h2>

          <div className="summary-item">
            <span>📚 Fact Score</span>
            <strong>--</strong>
          </div>

          <div className="summary-item">
            <span>🧠 Logic Score</span>
            <strong>--</strong>
          </div>

          <div className="summary-item">
            <span>✅ Validity Score</span>
            <strong>--</strong>
          </div>

          <hr />

          <div className="summary-item">
            <span>📊 Trust Score</span>
            <strong>--</strong>
          </div>

          <div className="status">
            Status : Waiting for Analysis
          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;