"""Chat service proxying messages to the AI orchestration service."""
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
ORCH_URL = os.getenv("AI_ORCH_URL", "http://ai-orchestration-service:5004")
DOC_URL = os.getenv("DOCUMENT_URL", "http://document-service:5005")


@app.route("/chat", methods=["POST"])
def chat():
    """Forward chat messages and files to the orchestration service."""
    files = {}
    if "file" in request.files:
        f = request.files["file"]
        files = {"file": (f.filename, f.stream, f.mimetype)}
    payload = request.form.to_dict()
    if files:
        requests.post(f"{DOC_URL}/upload", files=files)
    resp = requests.post(f"{ORCH_URL}/ask", json=payload)
    return jsonify(resp.json()), resp.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
