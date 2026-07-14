import "../Styles/History.css";

function History() {
  return (
    <div className="history-page">

      <div className="history-card">

        <h1>🕒 Recent Questions</h1>

        <p className="history-subtitle">
          Your previously asked questions will appear here.
        </p>

        <div className="history-box">

          <p className="empty-history">
            No recent questions found.
          </p>

        </div>

      </div>

    </div>
  );
}

export default History;