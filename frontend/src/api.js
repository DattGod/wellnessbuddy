export const askAgent = async (message) => {
  const response = await fetch("http://127.0.0.1:8000/api/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  return response.json();
};
