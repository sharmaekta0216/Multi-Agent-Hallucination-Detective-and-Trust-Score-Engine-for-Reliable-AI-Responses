import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

function Charts({
  fact,
  logic,
  evidence,
  hallucination,
  trust,
}) {

  const data = [
    { name: "Fact", score: fact },
    { name: "Logic", score: logic },
    { name: "Evidence", score: evidence },
    { name: "Hallucination", score: hallucination },
    { name: "Trust", score: trust },
  ];

  return (
    <div className="chart-card">

      <h2>Analysis Report</h2>

      <ResponsiveContainer
        width="100%"
        height={350}
      >

        <BarChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="name" />

          <YAxis domain={[0,100]} />

          <Tooltip />

          <Bar
            dataKey="score"
            fill="#2563eb"
            radius={[10,10,0,0]}
          />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
}

export default Charts;