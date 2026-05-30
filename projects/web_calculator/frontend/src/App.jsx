import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [result, setResult] = useState(null);
  const [operation, setOperation] = useState("");
  const [error, setError] = useState("");

  async function calculate(endpoint) {
    setError("");
    setResult(null);
    setOperation("");

    if (num1 === "" || num2 === "") {
      setError("Please enter both numbers.");
      return;
    }

    try {
      const response = await fetch(`${API_URL}/${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          num1: Number(num1),
          num2: Number(num2),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data.detail || "Something went wrong.");
        return;
      }

      setOperation(data.operation);
      setResult(data.result);
    } catch (err) {
      setError("Could not connect to the backend.");
    }
  }

  function clearCalculator() {
    setNum1("");
    setNum2("");
    setResult(null);
    setOperation("");
    setError("");
  }

  return (
    <main className="page">
      <section className="calculator-card">
        <div className="header">
          <p className="eyebrow">The fastest calculator on the Web</p>
          <h1>Web Calculator</h1>
          <p className="subtitle">
            Enter two numbers and choose an operation.
          </p>
        </div>

        <div className="input-group">
          <label>First Number</label>
          <input
            type="number"
            value={num1}
            onChange={(event) => setNum1(event.target.value)}
            placeholder="Example: 10"
          />
        </div>

        <div className="input-group">
          <label>Second Number</label>
          <input
            type="number"
            value={num2}
            onChange={(event) => setNum2(event.target.value)}
            placeholder="Example: 5"
          />
        </div>

        <div className="button-grid">
          <button onClick={() => calculate("add")}>Add</button>
          <button onClick={() => calculate("subtract")}>Subtract</button>
          <button onClick={() => calculate("multiply")}>Multiply</button>
          <button onClick={() => calculate("divide")}>Divide</button>
        </div>

        <button className="clear-button" onClick={clearCalculator}>
          Clear
        </button>

        {error && <div className="error-box">{error}</div>}

        {result !== null && (
          <div className="result-box">
            <p>{operation}</p>
            <h2>{result}</h2>
          </div>
        )}
      </section>
    </main>
  );
}

export default App;