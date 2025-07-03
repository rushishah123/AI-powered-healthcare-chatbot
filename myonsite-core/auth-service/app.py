"""Auth service providing authentication endpoints."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    """Dummy login endpoint returning a fake token."""
    # TODO: implement real authentication
    return jsonify({"token": "fake-token"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
