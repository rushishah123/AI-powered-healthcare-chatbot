from app import app


def test_queue_get():
    client = app.test_client()
    resp = client.get('/queue')
    assert resp.status_code == 200
