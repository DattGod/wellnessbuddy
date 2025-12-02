from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from agents.orchestrator import Orchestrator

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

orchestrator = Orchestrator()

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 422

    message = data["message"]
    try:
        response = orchestrator.run(message)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
