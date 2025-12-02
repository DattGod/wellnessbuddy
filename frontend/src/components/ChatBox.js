import React, { useState } from "react";
import { askAgent } from "../api";

function ChatBox() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;
    const res = await askAgent(input);
    setResponse(res.response);
  };

  return (
    <div style={{ marginTop: 30, padding: 20, background: "#fff", borderRadius: 8, border: "1px solid #ccc" }}>
      <h2>Ask Your AI Health Coach</h2>
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about workouts, diet, sleep, or mood"
        style={{ width: "100%", height: 100, padding: 10 }}
      />
      <button onClick={handleSend} style={{ marginTop: 10, padding: "10px 20px", background: "#1976d2", color: "#fff", border: "none", borderRadius: 6 }}>
        Send
      </button>

      {response && (
        <div style={{ marginTop: 20, padding: 15, background: "#e3f2fd", borderRadius: 6 }}>
          <strong>AI Response:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default ChatBox;
