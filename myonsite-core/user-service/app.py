"""User service managing user profiles."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/users/<user_id>")
def get_user(user_id: str):
    """Return a dummy user profile."""
    # TODO: fetch user from DB
    return jsonify({"user_id": user_id, "name": "John Doe"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
