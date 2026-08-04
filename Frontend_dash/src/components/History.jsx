// import { useEffect, useState } from "react";
// import "../Styles/History.css";

// function History() {

//   const [history, setHistory] = useState([]);

//   const userId = localStorage.getItem("user_id");

//   useEffect(() => {

//     if (!userId) {
//       setHistory([]);
//       return;
//     }

//     fetch(`https://multi-agent-hallucination-detective-xxxx.onrender.com/history/${userId}`)
//       .then((res) => res.json())
//       .then((data) => {
//         if (data.success) {
//           setHistory(data.history);
//         }
//       })
//       .catch((err) => console.log(err));

//   }, [userId]);

//   return (
//     <div className="history-page">

//       <div className="history-card">

//         <h1>🕒 Recent Questions</h1>

//         <p className="history-subtitle">
//           Your previously asked questions will appear here.
//         </p>

//         <div className="history-box">

//           {!userId ? (

//             <p className="empty-history">
//               Please login to view your history.
//             </p>

//           ) : history.length === 0 ? (

//             <p className="empty-history">
//               No recent questions found.
//             </p>

//           ) : (

//             history.map((item, index) => (

//               <div key={index} className="history-item">

//                 <h3>{item.query_text}</h3>

//                 <p>
//                   <strong>Response:</strong> {item.response_text}
//                 </p>

//                 <p>
//                   <strong>Trust Score:</strong> {item.final_trust_score}
//                 </p>

//                 <p>
//                   <strong>Trust Level:</strong> {item.trust_level}
//                 </p>

//                 <hr />

//               </div>

//             ))

//           )}

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

  const userId = localStorage.getItem("user_id");


  useEffect(() => {

    if (!userId) {
      setHistory([]);
      return;
    }


    fetch(
      `https://multi-agent-hallucination-detective-and.onrender.com/history/${userId}`
    )
      .then((res) => res.json())
      .then((data) => {

        if (data.success) {
          setHistory(data.history);
        }

      })
      .catch((err) => console.log(err));


  }, [userId]);



  return (

    <div className="history-page">

      <div className="history-card">


        <h1>🕒 Recent Questions</h1>


        <p className="history-subtitle">
          Your previously asked questions will appear here.
        </p>



        <div className="history-box">


          {!userId ? (

            <p className="empty-history">
              Please login to view your history.
            </p>


          ) : history.length === 0 ? (

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