import pytest
from src.app import app

@pytest.fixture
def client():
    """Fixture to set up the Flask test client"""
    with app.test_client() as client:
        yield client

def test_compute_correct_output(client):
    """Test that the output is correct for valid input"""
    response = client.post('/compute', json={"data": [5, 4, 6, 1]})
    assert response.status_code == 200
    assert response.json['output'] == 8.77

def test_insufficient_data(client):
    """Test the response when fewer than 3 numbers are provided"""
    response = client.post('/compute', json={"data": [5, 4]})
    assert response.status_code == 400
    assert "At least 3 numbers are required" in response.json['error']

def test_invalid_data_type(client):
    """Test the response when non-numeric data is provided"""
    response = client.post('/compute', json={"data": ["invalid", 4, 6]})
    assert response.status_code == 400
    assert "Input should be a list of numbers" in response.json['error']

def test_empty_data(client):
    """Test the response when an empty list is provided"""
    response = client.post('/compute', json={"data": []})
    assert response.status_code == 400
    assert "At least 3 numbers are required" in response.json['error']

def test_more_numbers(client):
    """Test the output when there are more than 3 numbers"""
    response = client.post('/compute', json={"data": [10, 20, 30, 5, 3]})
    assert response.status_code == 200
    assert response.json['output'] == 37.42

def test_edge_case(client):
    """Test the edge case with large numbers"""
    response = client.post('/compute', json={"data": [1000, 2000, 3000, 4, 5]})
    assert response.status_code == 200
    assert response.json['output'] == pytest.approx(3741.66, rel=1e-2)
