import pytest
from playwright.sync_api import sync_playwright

WEB_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture
def browser_instance():
    """Browser instance for web tests"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def web_page(browser_instance):
    """Page instance for web tests"""
    page = browser_instance.new_page()
    yield page
    page.close()