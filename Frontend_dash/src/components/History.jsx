// import "../Styles/History.css";

// function History() {
//   return (
//     <div className="history-page">

//       <div className="history-card">

//         <h1>🕒 Recent Questions</h1>

//         <p className="history-subtitle">
//           Your previously asked questions will appear here.
//         </p>

//         <div className="history-box">

//           <p className="empty-history">
//             No recent questions found.
//           </p>

//         </div>

//       </div>

//     </div>
//   );
// }

// export default History;
import { useEffect, useState } from "react";
import "../Styles/History.css";

function History() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const userId = localStorage.getItem("user_id");

    fetch(`http://127.0.0.1:8000/history/${userId}`)
      .then((res) => res.json())
      .then((data) => {
        if (data.success) {
          setHistory(data.history);
        }
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="history-page">
      <div className="history-card">

        <h1>🕒 Recent Questions</h1>

        <p className="history-subtitle">
          Your previously asked questions will appear here.
        </p>

        <div className="history-box">

          {history.length === 0 ? (
            <p className="empty-history">
              No recent questions found.
            </p>
          ) : (
            history.map((item, index) => (
              <div key={index} className="history-item">
                <h3>{item.query_text}</h3>

                <p>
                  <strong>Response:</strong> {item.response_text}
                </p>

                <p>
                  <strong>Trust Score:</strong> {item.final_trust_score}
                </p>

                <p>
                  <strong>Trust Level:</strong> {item.trust_level}
                </p>

                <hr />
              </div>
            ))
          )}

        </div>

      </div>
    </div>
  );
}

export default History;