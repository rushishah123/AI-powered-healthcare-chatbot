"""Approval service managing manual document reviews."""
from flask import Flask, jsonify, request

app = Flask(__name__)

queue = {}


@app.route('/queue', methods=['GET', 'POST'])
def queue_route():
    """List or add documents needing approval."""
    if request.method == 'POST':
        item = request.json
        queue[item['id']] = item
        return jsonify({'status': 'queued'}), 201
    return jsonify(list(queue.values()))


@app.route('/approve/<item_id>', methods=['POST'])
def approve(item_id: str):
    """Approve or reject an item."""
    decision = request.json.get('decision')
    queue.pop(item_id, None)
    # TODO: call notification service
    return jsonify({'id': item_id, 'decision': decision})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
