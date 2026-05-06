import pytest
import requests
from pydantic import BaseModel

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture
def api_client():
    """API client for Restful-Booker"""
    return requests.Session()

@pytest.fixture
def auth_token(api_client):
    """Get authentication token"""
    response = api_client.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"}
    )
    return response.json()["token"]

@pytest.fixture
def sample_booking():
    """Sample booking data"""
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-05-01",
            "checkout": "2024-05-02"
        },
        "additionalneeds": "Breakfast"
    }
