import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

function CircularScore({ title, value, color }) {
  return (
    <div className="circle-card">
      <div style={{ width: 130, height: 130 }}>
        <CircularProgressbar
          value={value}
          text={`${value}%`}
          styles={buildStyles({
            pathColor: color,
            textColor: "#2563eb",
            trailColor: "#e5e7eb",
            textSize: "16px",
          })}
        />
      </div>

      <h3>{title}</h3>
    </div>
  );
}

export default CircularScore;