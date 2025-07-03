from app import app


def test_get_user():
    client = app.test_client()
    response = client.get('/users/123')
    assert response.status_code == 200
    assert response.get_json()['user_id'] == '123'
