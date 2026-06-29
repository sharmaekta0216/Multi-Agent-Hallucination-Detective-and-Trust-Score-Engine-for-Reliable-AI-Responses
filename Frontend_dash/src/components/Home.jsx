import "../styles/Home.css";

function Home({ setPage }) {
  return (
    <div className="home">

      {/* Hero Section */}

      <section className="hero">

        <h1>Multi-Agent Hallucination Detector</h1>

        <h2>Trust Score Engine for Reliable AI Responses</h2>

        <p>
          Our project improves the reliability of AI-generated responses by
          using multiple intelligent agents that verify facts, analyze logic,
          validate information, and generate a Trust Score before presenting
          the final answer.
        </p>

        <button
          className="hero-btn"
          onClick={() => setPage("signup")}
        >
          Get Started
        </button>

      </section>

      {/* Features */}

      <section className="features">

        <div className="feature-card">
          <h3>📚 Fact Checker</h3>
          <p>
            Verifies factual claims using trusted knowledge sources and
            identifies unsupported statements.
          </p>
        </div>

        <div className="feature-card">
          <h3>🧠 Logic Checker</h3>
          <p>
            Detects logical inconsistencies and ensures the AI response follows
            correct reasoning.
          </p>
        </div>

        <div className="feature-card">
          <h3>✅ Validity Checker</h3>
          <p>
            Validates whether the generated answer is supported by sufficient
            evidence.
          </p>
        </div>

        <div className="feature-card">
          <h3>📊 Trust Score Engine</h3>
          <p>
            Combines results from all verification agents to generate an
            easy-to-understand Trust Score.
          </p>
        </div>

      </section>

      {/* Workflow */}

      <section className="workflow">

        <h2>Project Workflow</h2>

        <div className="workflow-box">

          <div>User Prompt</div>

          <span>↓</span>

          <div>AI Response</div>

          <span>↓</span>

          <div>Multi-Agent Verification</div>

          <span>↓</span>

          <div>Trust Score Generation</div>

          <span>↓</span>

          <div>Reliable Response</div>

        </div>

      </section>

    </div>
  );
}

export default Home;