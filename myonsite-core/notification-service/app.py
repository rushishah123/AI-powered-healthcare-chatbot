"""Notification service for sending simple notifications."""
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/notify', methods=['POST'])
def notify():
    """Print a notification to the console."""
    data = request.json
    print(f"Notify {data['user_id']} via {data['channel']}: {data['message']}")
    return jsonify({'status': 'sent'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
