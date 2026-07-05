function ScoreCard({title,value,color}){

return(

<div className="card">

<h3>{title}</h3>

<h1 style={{color}}>{value}%</h1>

<div className="progress">

<div
style={{
width:`${value}%`,
background:color
}}
></div>

</div>

</div>

)

}

export default ScoreCard;