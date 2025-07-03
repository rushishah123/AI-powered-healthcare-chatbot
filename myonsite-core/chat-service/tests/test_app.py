from app import app


def test_chat_proxy(monkeypatch):
    client = app.test_client()

    class DummyResponse:
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {"reply": "ok"}

    def dummy_post(*args, **kwargs):
        return DummyResponse()

    monkeypatch.setattr('requests.post', dummy_post)
    resp = client.post('/chat', data={'user_id': '1', 'message': 'hi'})
    assert resp.status_code == 200
