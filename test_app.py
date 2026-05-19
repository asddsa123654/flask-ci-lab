import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """Проверка базового эндпоинта Flask"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"status": "success", "message": " Flask API работает!"}
