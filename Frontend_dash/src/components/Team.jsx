// import "../styles/Team.css";


// function Team() {
//   const members = [
//     {
//       name: "Ekta Sharma",
//       role: "Team Leader",
//       branch: "CSE (AI)",
//       work: [
//         "Project Planning",
//         "Multi-Agent Architecture",
//         "Backend Integration",
//         "Workflow Management"
//       ]
//     },

//     {
//       name: "Falak Kumawat",
//       role: "Frontend Developer",
//       branch: "CSE (AI)",
//       work: [
//         "React UI Development",
//         "Responsive Design",
//         "Component Development",
//         "Frontend Integration"
//       ]
//     },

//     {
//       name: "Goon Bansal",
//       role: "Backend & Database Developer",
//       branch: "CSE",
//       work: [
//         "Database Design",
//         "API Integration",
//         "Data Management",
//         "Backend Support"
//       ]
//     },

//     {
//       name: "Kavita Bhati",
//       role: "Research & Documentation",
//       branch: "CSE",
//       work: [
//         "AI Research",
//         "Documentation",
//         "Testing",
//         "Performance Analysis"
//       ]
//     }
//   ];

//   return (
//     <div className="team-container">

//       <h1>Meet Our Team</h1>

//       <p className="team-subtitle">
//         A dedicated team working together to build reliable and trustworthy AI
//         systems through collaborative innovation.
//       </p>

//       <div className="team-grid">

//         {members.map((member, index) => (
//           <div className="team-card" key={index}>

//             <div className="avatar">
//               {member.name.charAt(0)}
//             </div>

//             <h2>{member.name}</h2>

//             <h4>{member.role}</h4>

//             <p>{member.branch}</p>

//             <hr />

//             <h3>Responsibilities</h3>

//             <ul>
//               {member.work.map((item, i) => (
//                 <li key={i}>✔ {item}</li>
//               ))}
//             </ul>

//           </div>
//         ))}

//       </div>

//     
import "../Styles/Team.css";

function Team() {

  const members = [
    {
      name: "Ekta Sharma",
      role: "Team Leader & Backend Developer",
      work: "Project Planning, Backend Development, Multi-Agent Architecture, FastAPI Integration"
    },
    {
      name: "Falak Kumawat",
      role: "Frontend Developer",
      work: "React UI, Responsive Design, Dashboard Development"
    },
    {
      name: "Goon Bansal",
      role: "Database Developer",
      work: "MySQL Database, Query Optimization, Data Management"
    },
    {
      name: "Kavita Bhati",
      role: "Documentation",
      work: "Project Documentation, Report Preparation, Presentation, Testing & Documentation Support"
    },
  ];

  return (
    <div className="team-page">

      <h1>👨‍💻 Meet Our Team</h1>

      <p className="team-subtitle">
        The talented team behind the Multi-Agent Hallucination Detection &
        Trust Score Engine.
      </p>

      <div className="team-grid">

        {members.map((member, index) => (
          <div className="team-card" key={index}>

            <div className="avatar">
              {member.name
                .split(" ")
                .map(word => word[0])
                .join("")}
            </div>

            <h2>{member.name}</h2>

            <h4>{member.role}</h4>

            <p>{member.work}</p>

          </div>
        ))}

      </div>

    </div>
  );
}

export default Team;