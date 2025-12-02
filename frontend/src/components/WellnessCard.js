import React from "react";

function WellnessCard() {
  return (
    <div style={{ marginTop: 20, padding: 20, background: "#fff", border: "1px solid #ccc", borderRadius: 8 }}>
      <h2>Your Daily Wellness Summary</h2>
      <ul>
        <li>Meals & Diet Plans</li>
        <li>Workout Recommendations</li>
        <li>Sleep Quality Insights</li>
        <li>Mood & Stress Levels</li>
      </ul>
      <p>Ask any question and I’ll guide you with AI-powered health coaching.</p>
    </div>
  );
}

export default WellnessCard;
