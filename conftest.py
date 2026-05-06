import pytest
import requests
from playwright.sync_api import sync_playwright

# API Fixtures
@pytest.fixture(scope="function")
def api_client():
    """HTTP client for API testing"""
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture
def base_url():
    """Base URL for Restful-Booker API"""
    return "https://restful-booker.herokuapp.com"

# Playwright Fixtures
@pytest.fixture(scope="function")
def browser():
    """Playwright browser instance"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Playwright page instance"""
    page = browser.new_page()
    yield page
    page.close()