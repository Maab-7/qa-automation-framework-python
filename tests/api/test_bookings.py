import pytest
from pydantic import BaseModel, Field

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str = None

class BookingResponse(BaseModel):
    bookingid: int
    booking: Booking

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.mark.api
class TestBookingAPI:
    
    def test_get_all_bookings(self, api_client):
        """Test GET /booking - Get all bookings"""
        response = api_client.get(f"{BASE_URL}/booking")
        
        assert response.status_code == 200
        bookings = response.json()
        assert len(bookings) > 0
        assert all("bookingid" in b for b in bookings)
    
    def test_create_booking(self, api_client, sample_booking):
        """Test POST /booking - Create booking"""
        response = api_client.post(
            f"{BASE_URL}/booking",
            json=sample_booking
        )
        
        assert response.status_code == 200
        result = BookingResponse(**response.json())
        assert result.booking.firstname == "John"
        assert result.bookingid > 0
        
        return result.bookingid
    
    def test_get_booking_by_id(self, api_client, sample_booking):
        """Test GET /booking/{id} - Get booking by ID"""
        # Create booking first
        create_response = api_client.post(
            f"{BASE_URL}/booking",
            json=sample_booking
        )
        booking_id = create_response.json()["bookingid"]
        
        # Get booking
        response = api_client.get(f"{BASE_URL}/booking/{booking_id}")
        
        assert response.status_code == 200
        booking = Booking(**response.json())
        assert booking.firstname == "John"
    
    def test_update_booking(self, api_client, sample_booking, auth_token):
        """Test PUT /booking/{id} - Update booking"""
        # Create booking
        create_response = api_client.post(
            f"{BASE_URL}/booking",
            json=sample_booking
        )
        booking_id = create_response.json()["bookingid"]
        
        # Update booking
        updated_data = {
            "firstname": "Jane",
            "lastname": "Smith",
            "totalprice": 222,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2024-06-01",
                "checkout": "2024-06-02"
            }
        }
        
        response = api_client.put(
            f"{BASE_URL}/booking/{booking_id}",
            json=updated_data,
            headers={"Cookie": f"token={auth_token}"}
        )
        
        assert response.status_code == 200
        booking = Booking(**response.json())
        assert booking.firstname == "Jane"
    
    def test_delete_booking(self, api_client, sample_booking, auth_token):
        """Test DELETE /booking/{id} - Delete booking"""
        # Create booking
        create_response = api_client.post(
            f"{BASE_URL}/booking",
            json=sample_booking
        )
        booking_id = create_response.json()["bookingid"]
        
        # Delete booking
        response = api_client.delete(
            f"{BASE_URL}/booking/{booking_id}",
            headers={"Cookie": f"token={auth_token}"}
        )
        
        assert response.status_code == 201
    
    @pytest.mark.parametrize("firstname,lastname", [
        ("Marco", "Alfaro"),
        ("Alice", "Johnson"),
        ("Bob", "Smith"),
    ])
    def test_create_multiple_bookings(self, api_client, firstname, lastname):
        """Test creating multiple bookings with different data"""
        payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-05-01",
                "checkout": "2024-05-02"
            }
        }
        
        response = api_client.post(
            f"{BASE_URL}/booking",
            json=payload
        )
        
        assert response.status_code == 200
        result = BookingResponse(**response.json())
        assert result.booking.firstname == firstname