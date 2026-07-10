/*function History({ history }) {

  return (

    <div className="history-card">

      <h2>Recent Queries</h2>

      {

      history.length===0?

      (

      <p>No History Available</p>

      )

      :

      (

      <ul>

      {

      history.map((item,index)=>(

      <li key={index}>

      {item}

      </li>

      ))

      }

      </ul>

      )

      }

    </div>

  );

}

export default History;*/

import "../Styles/History.css";

function History() {

  return (

    <div className="history-page">

      <div className="history-card">

        <h1>🕒 Recent Questions</h1>

        <p className="empty-history">

          No recent questions found.

        </p>

      </div>

    </div>

  );
}

export default History;