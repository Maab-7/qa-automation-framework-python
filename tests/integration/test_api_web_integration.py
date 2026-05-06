import pytest

@pytest.mark.integration
class TestAPIWebIntegration:
    """Integration tests: API + Web together"""
    
    def test_api_returns_bookings(self, api_client):
        """Test API returns booking data"""
        response = api_client.get("https://restful-booker.herokuapp.com/booking")
        
        assert response.status_code == 200
        bookings = response.json()
        assert isinstance(bookings, list)
        assert len(bookings) > 0
    
    def test_api_booking_has_required_fields(self, api_client):
        """Test booking has required fields"""
        response = api_client.get("https://restful-booker.herokuapp.com/booking?limit=1")
        
        assert response.status_code == 200
        bookings = response.json()
        
        if len(bookings) > 0:
            booking = bookings[0]
            assert "bookingid" in booking