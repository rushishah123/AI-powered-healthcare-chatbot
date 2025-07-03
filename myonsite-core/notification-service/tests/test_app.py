from app import app


def test_notify():
    client = app.test_client()
    resp = client.post('/notify', json={'user_id': '1', 'channel': 'email', 'message': 'hi'})
    assert resp.status_code == 200
