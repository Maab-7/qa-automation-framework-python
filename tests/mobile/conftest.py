import pytest
from appium import webdriver

@pytest.fixture
def ios_driver():
    """iOS Appium driver"""
    capabilities = {
        "platformName": "iOS",
        "automationName": "XCUITest",
        "deviceName": "iPhone 14",
        "app": "/path/to/app.app",
    }
    
    driver = webdriver.Remote(
        "http://localhost:4723",
        desired_capabilities=capabilities
    )
    yield driver
    driver.quit()
    