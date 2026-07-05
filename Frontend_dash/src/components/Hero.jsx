import "./styles/Hero.css";

function Hero() {
  return (
    <section className="hero">

      <div className="hero-left">

        <h1>
          Multi-Agent Hallucination
          Detection &
          Trust Score Engine
        </h1>

        <p>
          Analyze AI-generated responses using
          Fact Checking, Logic Analysis,
          Evidence Verification and Trust Scoring.
        </p>

        <button className="start-btn">
          Analyze Now
        </button>

      </div>

      <div className="hero-right">

        <img
          src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png"
          alt="AI Robot"
        />

      </div>

    </section>
  );
}

export default Hero;