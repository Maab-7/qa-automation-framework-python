import pytest

@pytest.mark.load
@pytest.mark.slow
@pytest.mark.skipif(True, reason="Load tests run separately with Locust CLI")
class TestLoadPerformance:
    """Load testing with Locust"""
    
    def test_load_placeholder(self):
        """Placeholder for load tests"""
        # Load tests run with:
        # locust -f tests/load/locustfile.py -u 10 -r 2 -t 60s
        pass