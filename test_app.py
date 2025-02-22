import pytest
from app import app  # Import the main Flask app from app.py

@pytest.fixture
def client():
    """Initialize the Flask test client"""
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:
        yield client  # Provide the test client to the tests

def test_home(client):
    """Test the home page ("/")"""
    response = client.get("/")
    assert response.status_code == 200  # Ensure the page loads successfully
    assert b"Hello, CI/CD!" in response.data  # Check if Hello,CI/CD! is returned

def test_api(client):
    """Test the API endpoint ("/api")"""
    response = client.get("/api")
    assert response.status_code == 200  # Ensure the API is reachable
    json_data = response.get_json()  # Get JSON response
    assert json_data == {"message": "This is a test API", "status": "success"}  # Validate response

def test_404(client):
    """Test the 404 error page for an invalid route"""
    response = client.get("/invalid-url")
    assert response.status_code == 404  # Ensure the correct error code is returned
    assert b"Page Not Found" in response.data  # Verify the error page contains expected text
