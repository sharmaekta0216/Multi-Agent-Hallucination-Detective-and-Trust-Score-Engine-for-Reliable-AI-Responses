// import { useState } from "react";
// import "../styles/Dashboard.css";

// function Dashboard() {

//   const [question, setQuestion] = useState("");

//   return (

//     <div className="dashboard">

//       <h1>AI Verification Dashboard</h1>

//       <p className="dashboard-subtitle">
//         Ask a question and let our multi-agent system verify the response before
//         generating a Trust Score.
//       </p>

//       <div className="dashboard-grid">

//         {/* LEFT SIDE */}

//         <div className="question-card">

//           <h2>Ask Your Question</h2>

//           <textarea
//             value={question}
//             onChange={(e) => setQuestion(e.target.value)}
//             placeholder="Example: What is Artificial Intelligence?"
//           />

//           <button className="analyze-btn">
//             Analyze Response
//           </button>

//         </div>

//         {/* RIGHT SIDE */}

//         <div className="summary-card">

//           <h2>Analysis Summary</h2>

//           <div className="summary-item">
//             <span>📚 Fact Score</span>
//             <strong>--</strong>
//           </div>

//           <div className="summary-item">
//             <span>🧠 Logic Score</span>
//             <strong>--</strong>
//           </div>

//           <div className="summary-item">
//             <span>✅ Validity Score</span>
//             <strong>--</strong>
//           </div>

//           <hr />

//           <div className="summary-item">
//             <span>📊 Trust Score</span>
//             <strong>--</strong>
//           </div>

//           <div className="status">
//             Status : Waiting for Analysis
//           </div>

//         </div>

//       </div>

//     </div>
//   );
// }

// export default Dashboard;
import { useState } from "react";
import "../styles/Dashboard.css";

function Dashboard() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeResponse = async () => {
    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: question,
        }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Unable to connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">

      <h1>AI Verification Dashboard</h1>

      <p className="dashboard-subtitle">
        Ask a question and let our multi-agent system verify the response before generating a Trust Score.
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

          <button
            className="analyze-btn"
            onClick={analyzeResponse}
          >
            {loading ? "Analyzing..." : "Analyze Response"}
          </button>

        </div>

        {/* RIGHT SIDE */}
        <div className="summary-card">

          <h2>Analysis Summary</h2>

          <div className="summary-item">
            <span>📚 Fact Score</span>
            <strong>{result ? result.fact.fact_score : "--"}</strong>
          </div>

          <div className="summary-item">
            <span>🧠 Logic Score</span>
            <strong>{result ? result.logic.logic_score : "--"}</strong>
          </div>

          <div className="summary-item">
            <span>✅ Validity Score</span>
            <strong>{result ? result.evidence.evidence_score : "--"}</strong>
          </div>

          <div className="summary-item">
            <span>⚠️ Hallucination Score</span>
            <strong>
              {result ? result.hallucination.hallucination_score : "--"}
            </strong>
          </div>

          <hr />

          <div className="summary-item">
            <span>📊 Trust Score</span>
            <strong>{result ? result.trust.trust_score : "--"}</strong>
          </div>

          <div className="status">
            {result
              ? `Status : ${result.trust.trust_level}`
              : "Status : Waiting for Analysis"}
          </div>

        </div>

      </div>

      {/* AI RESPONSE */}

      {result && (
        <div className="response-card">

          <h2>🤖 AI Response</h2>

          <p>{result.response.response}</p>

        </div>
      )}

      {/* VERIFICATION DETAILS */}

      {result && (
        <div className="response-card">

          <h2>Verification Details</h2>

          <p>
            <strong>Fact Check:</strong> {result.fact.message}
          </p>

          <p>
            <strong>Logic Check:</strong> {result.logic.message}
          </p>

          <p>
            <strong>Evidence Check:</strong> {result.evidence.message}
          </p>

          <p>
            <strong>Hallucination Check:</strong>{" "}
            {result.hallucination.message}
          </p>

        </div>
      )}

    </div>
  );
}

export default Dashboard;