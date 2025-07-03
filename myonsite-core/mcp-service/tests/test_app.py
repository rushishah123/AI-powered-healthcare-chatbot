from app import app


def test_get_mcp():
    client = app.test_client()
    resp = client.get('/mcp/1')
    assert resp.status_code == 200
    assert resp.get_json()['patient_id'] == '1'
