import pytest

@pytest.mark.mobile
@pytest.mark.skipif(True, reason="Requires local Appium server and device/simulator")
class TestIOSApp:
    """iOS Mobile tests using Appium (local development only)"""
    
    def test_app_placeholder(self):
        """Placeholder for mobile tests"""
        # Mobile tests run locally with:
        # appium &
        # pytest tests/mobile/ -v
        pass