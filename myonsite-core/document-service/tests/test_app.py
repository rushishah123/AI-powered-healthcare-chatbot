from app import app


def test_upload(monkeypatch):
    client = app.test_client()

    data = {'file': (open(__file__, 'rb'), 'test.txt')}
    resp = client.post('/upload', data=data)
    assert resp.status_code == 200
