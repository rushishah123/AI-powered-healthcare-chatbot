"""Service providing Model Context Protocol data."""
from flask import Flask, jsonify
from datetime import datetime
from shared.mcp_models import MCP, ContextBlock, Demographics

app = Flask(__name__)


@app.route('/mcp/<patient_id>')
def get_mcp(patient_id: str):
    """Return a dummy MCP object for a patient."""
    demo = Demographics(patient_id=patient_id, name='Jane Doe', age=30, gender='F')
    mcp = MCP(
        patient_id=patient_id,
        timestamp=datetime.utcnow(),
        context_blocks=[ContextBlock(type='demographics', payload=demo)]
    )
    return jsonify(mcp.dict())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)
