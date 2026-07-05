import "./Loader.css";

function Loader() {
  return (
    <div className="loader-container">

      <div className="spinner"></div>

      <h3>Analyzing Response...</h3>

      <p>Please wait while our AI agents verify your response.</p>

    </div>
  );
}

export default Loader;