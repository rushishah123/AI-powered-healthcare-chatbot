from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_ask(monkeypatch):
    def dummy_get(url):
        class R:
            def json(self):
                return {}
        return R()
    monkeypatch.setattr('requests.get', dummy_get)
    resp = client.post('/ask', json={'user_id': '1', 'message': 'hello'})
    assert resp.status_code == 200
