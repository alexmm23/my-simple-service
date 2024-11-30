import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_about_page(client):
    """Test the about page."""
    response = client.get('/about')
    assert response.status_code == 200
    assert response.json == {"message": "About Us"}