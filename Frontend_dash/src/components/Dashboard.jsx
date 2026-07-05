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





























import React, { useState } from "react";
import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  LineChart,
  Line,
} from "recharts";

import CircularScore from "./CircularScore";

function Dashboard() {
  const [active, setActive] = useState("home");

  const stats = [
    { title: "Users", value: 1200 },
    { title: "Revenue", value: "$8.5K" },
    { title: "Orders", value: 320 },
    { title: "Feedback", value: "98%" },
  ];

  const chartData = [
    { name: "Jan", value: 400 },
    { name: "Feb", value: 800 },
    { name: "Mar", value: 600 },
    { name: "Apr", value: 1200 },
  ];

  const ads = [
    { title: "🔥 Upgrade Pro Plan", desc: "Get advanced analytics & AI insights" },
    { title: "⚡ Fast API Hosting", desc: "Deploy backend in seconds" },
    { title: "📊 Premium Dashboard UI", desc: "Unlock pro templates" },
  ];

  return (
    <div className="dashboard">

      {/* Sidebar */}
      <aside className="sidebar">
        <h2>MyApp</h2>

        <ul>
          <li onClick={() => setActive("home")}>Home</li>
          <li onClick={() => setActive("charts")}>Charts</li>
          <li onClick={() => setActive("ads")}>Ads</li>
          <li onClick={() => setActive("history")}>History</li>
        </ul>
      </aside>

      {/* Main */}
      <main className="main">

        {/* Navbar */}
        <div className="navbar">
          <h1>Dashboard</h1>
          <button className="login-btn">Login</button>
        </div>

        {/* HOME */}
        {active === "home" && (
          <>
            <div className="top-section">
              <CircularScore title="Trust Score" value={82} color="#2563eb" />
            </div>

            <div className="stats">
              {stats.map((s, i) => (
                <div className="card" key={i}>
                  <h3>{s.title}</h3>
                  <h1>{s.value}</h1>
                </div>
              ))}
            </div>
          </>
        )}

        {/* CHARTS */}
        {active === "charts" && (
          <div className="charts">

            <div className="chart-box">
              <h3>Revenue Trend</h3>

              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Line dataKey="value" stroke="#2563eb" />
                </LineChart>
              </ResponsiveContainer>
            </div>

            <div className="chart-box">
              <h3>Users Growth</h3>

              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={chartData}>
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="value" fill="#22c55e" />
                </BarChart>
              </ResponsiveContainer>
            </div>

          </div>
        )}

        {/* ADS SECTION */}
        {active === "ads" && (
          <div className="ads-section">
            <h2>Sponsored Ads</h2>

            <div className="ads-grid">
              {ads.map((ad, i) => (
                <div className="ad-card" key={i}>
                  <h3>{ad.title}</h3>
                  <p>{ad.desc}</p>
                  <button>Learn More</button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* HISTORY */}
        {active === "history" && (
          <div className="history">
            <h2>Recent Activity</h2>
            <ul>
              <li>User analyzed query #1</li>
              <li>AI response generated</li>
              <li>Trust score calculated</li>
            </ul>
          </div>
        )}

      </main>
    </div>
  );
}

export default Dashboard;