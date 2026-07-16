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
// import { useState } from "react";
// import "../styles/Dashboard.css";

// function Dashboard() {
//   const [question, setQuestion] = useState("");
//   const [result, setResult] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const analyzeResponse = async () => {
//     if (!question.trim()) {
//       alert("Please enter a question.");
//       return;
//     }

//     try {
//       setLoading(true);

//       const response = await fetch("http://127.0.0.1:8000/analyze", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//           query: question,
//         }),
//       });

//       const data = await response.json();
//       setResult(data);
//     } catch (error) {
//       console.error(error);
//       alert("Unable to connect to backend.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="dashboard">

//       <h1>AI Verification Dashboard</h1>

//       <p className="dashboard-subtitle">
//         Ask a question and let our multi-agent system verify the response before generating a Trust Score.
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

//           <button
//             className="analyze-btn"
//             onClick={analyzeResponse}
//           >
//             {loading ? "Analyzing..." : "Analyze Response"}
//           </button>

//         </div>

//         {/* RIGHT SIDE */}
//         <div className="summary-card">

//           <h2>Analysis Summary</h2>

//           <div className="summary-item">
//             <span>📚 Fact Score</span>
//             <strong>{result ? result.fact.fact_score : "--"}</strong>
//           </div>

//           <div className="summary-item">
//             <span>🧠 Logic Score</span>
//             <strong>{result ? result.logic.logic_score : "--"}</strong>
//           </div>

//           <div className="summary-item">
//             <span>✅ Validity Score</span>
//             <strong>{result ? result.evidence.evidence_score : "--"}</strong>
//           </div>

//           <div className="summary-item">
//             <span>⚠️ Hallucination Score</span>
//             <strong>
//               {result ? result.hallucination.hallucination_score : "--"}
//             </strong>
//           </div>

//           <hr />

//           <div className="summary-item">
//             <span>📊 Trust Score</span>
//             <strong>{result ? result.trust.trust_score : "--"}</strong>
//           </div>

//           <div className="status">
//             {result
//               ? `Status : ${result.trust.trust_level}`
//               : "Status : Waiting for Analysis"}
//           </div>

//         </div>

//       </div>

//       {/* AI RESPONSE */}

//       {result && (
//         <div className="response-card">

//           <h2>🤖 AI Response</h2>

//           <p>{result.response.response}</p>

//         </div>
//       )}

//       {/* VERIFICATION DETAILS */}

//       {result && (
//         <div className="response-card">

//           <h2>Verification Details</h2>

//           <p>
//             <strong>Fact Check:</strong> {result.fact.message}
//           </p>

//           <p>
//             <strong>Logic Check:</strong> {result.logic.message}
//           </p>

//           <p>
//             <strong>Evidence Check:</strong> {result.evidence.message}
//           </p>

//           <p>
//             <strong>Hallucination Check:</strong>{" "}
//             {result.hallucination.message}
//           </p>

//         </div>
//       )}

//     </div>
//   );
// }

// export default Dashboard;




















// <div className="circle-grid">

//             <CircularScore
//               title="Fact Score"
//               value={result.fact_score}
//               color="#22c55e"
//             />

//             <CircularScore
//               title="Logic Score"
//               value={result.logic_score}
//               color="#2563eb"
//             />

//             <CircularScore
//               title="Evidence Score"
//               value={result.evidence_score}
//               color="#f59e0b"
//             />

//             <CircularScore
//               title="Hallucination"
//               value={result.hallucination_score}
//               color="#ef4444"
//             />

//             <CircularScore
//               title="Trust Score"
//               value={result.trust_score}
//               color="#8b5cf6"
//             />

//           </div>

//           <Charts
//             fact={result.fact_score}
//             logic={result.logic_score}
//             evidence={result.evidence_score}
//             hallucination={result.hallucination_score}
//             trust={result.trust_score}
//           />

//           <div className="action-buttons">

//             <button
//               className="download-btn"
//               onClick={() => window.print()}
//             >
//               📄 Download Report
//             </button>

//             <button
//               className="copy-btn"
//               onClick={copyResult}
//             >
//               📋 Copy Result
//             </button>

//           </div>

//           <div className="info-grid">

//             <div className="info-card">
//               <h3>Processing Time</h3>
//               <p>
//                 {result.processing_time
//                   ? `${result.processing_time} sec`
//                   : "0.45 sec"}
//               </p>
//             </div>

//             <div className="info-card">
//               <h3>Backend Status</h3>
//               <p className="success">
//                 🟢 Connected
//               </p>
//             </div>

//             <div className="info-card">
//               <h3>Total Queries</h3>
//               <p>{history.length}</p>
//             </div>

//           </div>

//           <div className="summary-card">

//             <h2>Analysis Summary</h2>

//             <p>
//               This response has been analyzed using
//               Fact Checking, Logic Verification,
//               Evidence Analysis and Hallucination Detection.
//             </p>

//             <h3>
//               Overall Trus
// //     import { useState } from "react";
// // import "../styles/Dashboard.css";

// // function Dashboard() {
// //   const [question, setQuestion] = useState("");
// //   const [result, setResult] = useState(null);
// //   const [loading, setLoading] = useState(false);
// //   const [error, setError] = useState("");

// //   const analyzeResponse = async () => {
// //     if (!question.trim()) {
// //       alert("Please enter a question.");
// //       return;
// //     }

// //     setLoading(true);
// //     setError("");
// //     setResult(null);

// //     try {
// //       const response = await fetch("http://127.0.0.1:8000/analyze", {
// //         method: "POST",
// //         headers: {
// //           "Content-Type": "application/json",
// //         },
// //         body: JSON.stringify({
// //           question: question,
// //         }),
// //       });

// //       const data = await response.json();

// //       if (!response.ok) {
// //         throw new Error(data.detail || "Server Error");
// //       }

// //       setResult(data);
// //     } catch (err) {
// //       console.error(err);
// //       setError("Backend not connected or server error.");
// //     } finally {
// //       setLoading(false);
// //     }
// //   };

// //   return (
// //     <div className="dashboard-container">

// //       <h1>🤖 Multi-Agent Hallucination Detection</h1>

// //       <textarea
// //         rows="6"
// //         placeholder="Enter your question..."
// //         value={question}
// //         onChange={(e) => setQuestion(e.target.value)}
// //       />

// //       <button onClick={analyzeResponse}>
// //         {loading ? "Analyzing..." : "Analyze"}
// //       </button>

// //       {error && (
// //         <div className="error-box">
// //           {error}
// //         </div>
// //       )}

// //       {result && (
// //         <>

// //           <div className="response-card">
// //             <h2>🤖 AI Response</h2>
// //             <p>{result.answer}</p>
// //           </div>

// //           <div className="score-grid">

// //             <div className="card">
// //               <h3>Trust Score</h3>
// //               <h1>{result.trust_score}%</h1>
// //             </div>

// //             <div className="card">
// //               <h3>Trust Level</h3>
// //               <h1>{result.trust_level}</h1>
// //             </div>

// //             <div className="card">
// //               <h3>Fact Score</h3>
// //               <h1>{result.fact_score}%</h1>
// //             </div>

// //             <div className="card">
// //               <h3>Logic Score</h3>
// //               <h1>{result.logic_score}%</h1>
// //             </div>

// //             <div className="card">
// //               <h3>Evidence Score</h3>
// //               <h1>{result.evidence_score}%</h1>
// //             </div>

// //             <div className="card">
// //               <h3>Hallucination Score</h3>
// //               <h1>{result.hallucination_score}%</h1>
// //             </div>

// //           </div>

// //         </>
// //       )}

// //     </div>
// //   );
// // }

// // export default Dashboard;
// // import React, { useState } from "react";
// // import "./Dashboard.css";

// // function Dashboard() {
// //   const [query, setQuery] = useState("");
// //   const [loading, setLoading] = useState(false);
// //   const [result, setResult] = useState(null);
// //   const [error, setError] = useState("");

// //   const handleAnalyze = async () => {
// //     if (!query.trim()) {
// //       setError("Please enter a question.");
// //       return;
// //     }

// //     setLoading(true);
// //     setError("");
// //     setResult(null);

// //     try {
// //       const response = await fetch("http://127.0.0.1:8000/analyze", {
// //         method: "POST",
// //         headers: {
// //           "Content-Type": "application/json",
// //         },
// //         body: JSON.stringify({
// //           query: query,
// //         }),
// //       });

// //       if (!response.ok) {
// //         throw new Error("Backend not connected or server error.");
// //       }

// //       const data = await response.json();
// //       setResult(data);
// //     } catch (err) {
// //       setError(err.message);
// //     }

//     setLoading(false);
//   };

//   return (
//     <div className="dashboard-container">
//       <h1>🤖 Multi-Agent Hallucination Detection</h1>

//       <textarea
//         rows="7"
//         placeholder="Enter your question here..."
//         value={query}
//         onChange={(e) => setQuery(e.target.value)}
//       />

//       <button onClick={handleAnalyze} disabled={loading}>
//         {loading ? "Analyzing..." : "Analyze"}
//       </button>

//       {error && <div className="error-box">{error}</div>}

//       {result && (
//         <>
//           <div className="response-card">
//             <h2>AI Response</h2>
//             <p>{result.response}</p>
//           </div>

//           <div className="score-grid">
//             <div className="card">
//               <h3>Fact Score</h3>
//               <h1>{result.fact_score}%</h1>
//             </div>

//             <div className="card">
//               <h3>Logic Score</h3>
//               <h1>{result.logic_score}%</h1>
//             </div>

//             <div className="card">
//               <h3>Evidence Score</h3>
//               <h1>{result.evidence_score}%</h1>
//             </div>

//             <div className="card">
//               <h3>Hallucination Score</h3>
//               <h1>{result.hallucination_score}%</h1>
//             </div>

//             <div className="card">
//               <h3>Trust Score</h3>
//               <h1>{result.trust_score}%</h1>
//             </div>

//             <div className="card">
//               <h3>Trust Level</h3>
//               <h1>{result.trust_level}</h1>
//             </div>
//           </div>
//         </>
//       )}
//     </div>
//   );
// }

// export default Dashboard;
























import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { useState } from "react";
import "../Styles/Dashboard.css";
import CircularScore from "./CircularScore";

function Dashboard() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const analyzeResponse = async () => {
    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: 1,
          question: question,
        }),
      });

      const data = await response.json();

      console.log("Response:", data);

      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  const chartData = result
    ? [
        {
          agent: "Fact",
          score: result.fact_score,
        },
        {
          agent: "Logic",
          score: result.logic_score,
        },
        {
          agent: "Evidence",
          score: result.evidence_score,
        },
        {
          agent: "Hallucination",
          score: 100 - result.hallucination_score,
        },
      ]
    : [];

  return (
    <div className="dashboard">

      <div className="dashboard-header">
        <h1>🤖 Multi-Agent Hallucination Detector</h1>
        <p>Trust Score Engine for Reliable AI Responses</p>
      </div>

      <div className="question-card">

        <textarea
          placeholder="Ask any question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button onClick={analyzeResponse}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>

      </div>

      {result && (
        <>

          {/* Trust Score */}

          <div className="score-section">

            <CircularScore
              title="Trust Score"
              value={result.trust_score}
            />

            <div className="score-grid">

              <div className="card">
                <h3>Fact Score</h3>
                <h2>{result.fact_score}</h2>
              </div>

              <div className="card">
                <h3>Logic Score</h3>
                <h2>{result.logic_score}</h2>
              </div>

              <div className="card">
                <h3>Evidence Score</h3>
                <h2>{result.evidence_score}</h2>
              </div>

              <div className="card">
                <h3>Hallucination</h3>
                <h2>{result.hallucination_score}</h2>
              </div>

            </div>

          </div>

          {/* AI Response */}

          <div className="response-card">

            <h2>Question</h2>

            <p>{result.question}</p>

            <h2>AI Response</h2>

            {/* <p>{result.ai_response}</p> */}
            <div className="markdown-response">
  <ReactMarkdown remarkPlugins={[remarkGfm]}>
    {result.ai_response}
  </ReactMarkdown>
</div>

            <h3>
              Trust Level :
              <span> {result.trust_level}</span>
            </h3>

          </div>          {/* Analysis Report */}

          <div className="response-card">

            <h2>Analysis Report</h2>

            <div className="analysis-item">
              <h3>✅ Fact Check</h3>
              <p>{result.fact_message}</p>
            </div>

            <div className="analysis-item">
              <h3>🧠 Logic Analysis</h3>
              <p>{result.logic_message}</p>
            </div>

            <div className="analysis-item">
              <h3>📚 Evidence Analysis</h3>
              <p>{result.evidence_message}</p>
            </div>

            <div className="analysis-item">
              <h3>🚨 Hallucination Analysis</h3>
              <p>{result.hallucination_message}</p>
            </div>

          </div>

          {/* Agent Performance Chart */}

          <div className="chart-card">

            <h2>Agent Performance</h2>

            <ResponsiveContainer width="100%" height={350}>

              <BarChart data={chartData}>

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="agent" />

                <YAxis domain={[0, 100]} />

                <Tooltip />

                <Bar
                  dataKey="score"
                  radius={[8, 8, 0, 0]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </>
      )}

    </div>
  );
}

export default Dashboard;