import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_search_news(client):
    response = client.get('/search?q=Python')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_search_news_missing_query(client):
    response = client.get('/search')
    assert response.status_code == 400
    assert response.json['error'] == 'Missing query parameter "q"'

def test_top_news(client):
    response = client.get('/top-news')
    assert response.status_code == 200
    assert isinstance(response.json, list)
