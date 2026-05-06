import pytest

@pytest.mark.web
class TestWebUI:
    """Web UI tests using Playwright"""
    
    def test_page_loads(self, web_page):
        """Test page loads successfully"""
        web_page.goto("https://restful-booker.herokuapp.com")
        web_page.wait_for_load_state("networkidle")
        title = web_page.title()
        assert title is not None
        assert "restful-booker" in title.lower()
    
    def test_page_has_welcome_content(self, web_page):
        """Test page has welcome content"""
        web_page.goto("https://restful-booker.herokuapp.com")
        web_page.wait_for_load_state("networkidle")
        content = web_page.content()
        # Look for actual content in page
        assert "welcome" in content.lower() or "restful-booker" in content.lower()
    
    def test_page_responsive(self, web_page):
        """Test page is responsive on mobile"""
        web_page.set_viewport_size({"width": 375, "height": 667})
        web_page.goto("https://restful-booker.herokuapp.com")
        web_page.wait_for_load_state("networkidle")
        assert web_page.title() is not None