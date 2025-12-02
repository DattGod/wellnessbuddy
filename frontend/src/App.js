import React, { useState } from "react";
import ChatBox from "./components/ChatBox";
import WellnessCard from "./components/WellnessCard";

function App() {
  return (
    <div style={{ padding: 20, maxWidth: 800, margin: "0 auto" }}>
      <h1 style={{ textAlign: "center" }}>WellnessBuddy — AI Health & Wellness Coach</h1>
      <WellnessCard />
      <ChatBox />
    </div>
  );
}

export default App;
