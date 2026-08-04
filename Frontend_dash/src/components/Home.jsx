import "../Styles/Home.css";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home">

      {/* ================= HERO ================= */}

      <section className="hero">

        <span className="hero-tag">
          🚀 AI Powered • Multi-Agent Verification • Trust Scoring
        </span>

        <h1>
          Multi-Agent Hallucination Detective
        </h1>

        <h2>
          Delivering Reliable AI Responses with Intelligent Multi-Agent Validation
        </h2>

        <p>
          Artificial Intelligence can generate impressive responses, but can
          they always be trusted?
          <br /><br />

          Our Multi-Agent Hallucination Detector enhances AI reliability by
          combining the intelligence of multiple specialized agents that
          independently verify facts, analyze logical consistency, validate
          supporting evidence, detect hallucinations, and evaluate adversarial
          vulnerabilities before presenting the final answer.

          <br /><br />

          Every response is accompanied by a comprehensive Trust Score,
          enabling users to confidently distinguish trustworthy information
          from potentially misleading AI-generated content.
        </p>

        <div className="hero-buttons">

          <Link to="/login">
            <button className="hero-btn">
              Get Started
            </button>
          </Link>

          <Link to="/about">
            <button className="hero-btn secondary-btn">
              Learn More
            </button>
          </Link>

        </div>

      </section>

      {/* ================= WHY CHOOSE ================= */}

      <section className="workflow">

        <h2>Why Choose Our Platform?</h2>

        <div className="workflow-box">

          <div>
            🔍<br />
            AI responses are independently verified
          </div>

          <span>→</span>

          <div>
            🤖<br />
            Multiple intelligent agents analyze every answer
          </div>

          <span>→</span>

          <div>
            📊<br />
            A transparent Trust Score is generated
          </div>

          <span>→</span>

          <div>
            ✅<br />
            Users receive reliable AI responses
          </div>

        </div>

      </section>

      {/* ================= FEATURES ================= */}

      <section className="features">

        <div className="feature-card">

          <h3>📚 Fact Verification</h3>

          <p>
            Cross-checks factual claims against reliable knowledge sources,
            identifying misinformation and unsupported statements before the
            response reaches the user.
          </p>

        </div>

        <div className="feature-card">

          <h3>🧠 Logical Reasoning</h3>

          <p>
            Evaluates reasoning patterns, detects inconsistencies, and ensures
            responses follow coherent and meaningful logical structures.
          </p>

        </div>

        <div className="feature-card">

          <h3>📖 Evidence Validation</h3>

          <p>
            Determines whether the generated response is backed by sufficient,
            relevant, and credible supporting evidence.
          </p>

        </div>

        <div className="feature-card">

          <h3>🚨 Hallucination Detection</h3>

          <p>
            Identifies fabricated information, misleading statements, and AI
            hallucinations that may reduce the reliability of generated
            responses.
          </p>

        </div>

        <div className="feature-card">

          <h3>⚔️ Adversarial Analysis</h3>

          <p>
            Evaluates AI robustness against malicious prompts, jailbreak
            attempts, and manipulation techniques.
          </p>

        </div>

        <div className="feature-card">

          <h3>📊 Trust Score Engine</h3>

          <p>
            Combines outputs from every verification agent into a single,
            interpretable Trust Score, enabling users to instantly evaluate the
            credibility of every AI response.
          </p>

        </div>

      </section>

      {/* ================= HOW IT WORKS ================= */}

      <section className="workflow">

        <h2>How It Works</h2>

        <div className="workflow-box">

          <div>💬 User Prompt</div>

          <span>→</span>

          <div>🤖 AI Response</div>

          <span>→</span>

          <div>🧠 Multi-Agent Verification</div>

          <span>→</span>

          <div>📊 Trust Score Generation</div>

          <span>→</span>

          <div>✅ Reliable & Verified Response</div>

        </div>

      </section>

      {/* ================= FINAL CTA ================= */}

      <section className="hero">

        <h2>
          Experience Reliable Artificial Intelligence
        </h2>

        <p>
          Discover a smarter way to interact with AI where every response is
          analyzed, verified, and scored before reaching you. Build confidence
          in AI-generated information through transparency and intelligent
          multi-agent validation.
        </p>

        <Link to="/login">
          <button className="hero-btn">
            Start Exploring →
          </button>
        </Link>

      </section>

    </div>
  );
}

export default Home;