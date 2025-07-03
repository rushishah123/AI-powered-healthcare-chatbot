"""Document service handling uploads and OCR."""
from flask import Flask, request, jsonify

app = Flask(__name__)

pending_docs = {}


@app.route("/upload", methods=["POST"])
def upload():
    """Upload a document and attempt OCR/classification."""
    file = request.files.get('file')
    # TODO: run OCR with pytesseract
    doc_type = 'lab_report'  # TODO: implement classification
    fields = {"sample": "data"}
    confidence = 0.5  # TODO: compute real confidence
    result = {"type": doc_type, "fields": fields, "confidence": confidence}
    if confidence < 0.8:
        pending_docs['1'] = result
        # TODO: call approval service
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
