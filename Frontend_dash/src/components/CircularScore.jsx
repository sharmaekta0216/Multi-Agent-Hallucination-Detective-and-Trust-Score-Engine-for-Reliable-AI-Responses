// import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
// import "react-circular-progressbar/dist/styles.css";

// function CircularScore({ title, value, color }) {
//   return (
//     <div className="circle-card">
//       <div style={{ width: 130, height: 130 }}>
//         <CircularProgressbar
//           value={value}
//           text={`${value}%`}
//           styles={buildStyles({
//             pathColor: color,
//             textColor: "#2563eb",
//             trailColor: "#e5e7eb",
//             textSize: "16px",
//           })}
//         />
//       </div>

//       <h3>{title}</h3>
//     </div>
//   );
// }

// export default CircularScore;
import React from "react";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/Styles.css";

function CircularScore({ title, value }) {
  return (
    <div
      style={{
        width: "220px",
        background: "white",
        padding: "25px",
        borderRadius: "20px",
        boxShadow: "0 8px 20px rgba(0,0,0,0.2)",
        textAlign: "center",
      }}
    >
      <h3 style={{ color: "#111827", marginBottom: "20px" }}>
        {title}
      </h3>

      <CircularProgressbar
        value={value}
        text={`${value}%`}
        styles={buildStyles({
          textColor: "#2563eb",
          pathColor: "#2563eb",
          trailColor: "#e5e7eb",
        })}
      />
    </div>
  );
}

export default CircularScore;