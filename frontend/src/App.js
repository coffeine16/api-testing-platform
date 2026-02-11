import React, { useState } from "react";

function App() {
  const [specId, setSpecId] = useState("");
  const [report, setReport] = useState(null);

  const runScan = async () => {
    const res = await fetch(`http://localhost:8000/api/run/${specId}`, {
      method: "POST",
    });
    const data = await res.json();
    setReport(data.result);
  };

  return (
    <div style={{ padding: 30 }}>
      <h1>API Security Dashboard</h1>

      <input
        placeholder="Enter Spec ID"
        value={specId}
        onChange={(e) => setSpecId(e.target.value)}
      />

      <button onClick={runScan}>Run Scan</button>

      {report && (
        <>
          <h2>Summary</h2>
          <p>High Risks: {report.summary.high_risks}</p>
          <p>Failed Tests: {report.summary.failed_tests}</p>
          <p>Deployment: {report.summary.deployment_status}</p>

          <h2>Security Findings</h2>
          {report.security_findings.map((f, i) => (
            <div key={i}>
              <strong>{f.endpoint}</strong> — {f.issue}
            </div>
          ))}

          <h2>API Test Results</h2>
          {report.api_test_results.map((r, i) => (
            <div key={i}>
              {r.endpoint} — Status: {r.status_code}
            </div>
          ))}

          <h2>Recommendations</h2>
          {report.recommendations.map((rec, i) => (
            <p key={i}>{rec}</p>
          ))}
        </>
      )}

    </div>
  );
}

export default App;
