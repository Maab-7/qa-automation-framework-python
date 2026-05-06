from locust import HttpUser, task, between
import json

class BookingUser(HttpUser):
    """Simulated user for load testing"""
    
    wait_time = between(1, 3)
    
    @task(3)
    def get_bookings(self):
        """Get all bookings (3x weight)"""
        self.client.get("/booking")
    
    @task(2)
    def create_booking(self):
        """Create booking (2x weight)"""
        payload = {
            "firstname": "Load",
            "lastname": "Test",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-05-01",
                "checkout": "2024-05-02"
            }
        }
        self.client.post("/booking", json=payload)
    
    @task(1)
    def get_booking_detail(self):
        """Get specific booking (1x weight)"""
        self.client.get("/booking/1")
    
    def on_start(self):
        """Called when user starts"""
        print("User started")
    
    def on_stop(self):
        """Called when user stops"""
        print("User stopped")