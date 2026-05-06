class RestfulBookerPage:
    """Page Object for Restful Booker Web"""
    
    def __init__(self, page):
        self.page = page
        self.url = "https://restful-booker.herokuapp.com"
        
        # Locators
        self.btn_add_booking = "#addbtn"
        self.input_firstname = "input[name='firstname']"
        self.input_lastname = "input[name='lastname']"
        self.input_price = "input[name='totalprice']"
        self.input_checkin = "input[name='checkin']"
        self.input_checkout = "input[name='checkout']"
        self.btn_save = "#savebtn"
        self.table_bookings = "table tbody tr"
    
    def navigate(self):
        """Navigate to Restful Booker"""
        self.page.goto(self.url)
    
    def click_add_booking(self):
        """Click add booking button"""
        self.page.click(self.btn_add_booking)
    
    def fill_booking_form(self, firstname, lastname, price, checkin, checkout):
        """Fill booking form"""
        self.page.fill(self.input_firstname, firstname)
        self.page.fill(self.input_lastname, lastname)
        self.page.fill(self.input_price, str(price))
        self.page.fill(self.input_checkin, checkin)
        self.page.fill(self.input_checkout, checkout)
    
    def save_booking(self):
        """Click save button"""
        self.page.click(self.btn_save)
    
    def get_booking_count(self):
        """Get number of bookings in table"""
        return self.page.locator(self.table_bookings).count()
    
    def is_page_loaded(self):
        """Check if page is loaded"""
        self.page.wait_for_load_state("networkidle")
        return self.page.title() is not None