# tests/users_e2e_test.py
from fastapi.testclient import TestClient
from src.main import app  # Adjusted import path for main.py

client = TestClient(app)

USER_ENDPOINT = "/api/v1/users/1"


def test_user():
    res = client.get(USER_ENDPOINT)
    assert res.status_code == 200

    response_data = res.json()

    # Check if 'data' key exists in the JSON response
    assert "data" in response_data

    # Access the 'data' object within the response
    data = response_data["data"]

    # Check if 'id' and 'name' keys exist in the user data
    assert "id" in data
    assert "name" in data

    # Optionally, you can check if the values of 'id' and 'name' are of the
    # expected types
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
