from app import app


def test_login():
    client = app.test_client()
    response = client.post('/login')
    assert response.status_code == 200
    assert 'token' in response.get_json()
