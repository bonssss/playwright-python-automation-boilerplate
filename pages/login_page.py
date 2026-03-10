from playwright.sync_api import Page
from pages.base_page import BasePage
from config.config import USER_NAME, PASSWORD
import time

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.phone_input = page.locator("(//input[@placeholder='Email or Username'])[1]")
        self.password_input = page.locator("(//input[@placeholder='Password'])[1]")
        self.login_button = page.get_by_role("button", name="Sign In")
    def enter_phone(self):
        self.phone_input.fill(USER_NAME)
        
    def enter_password(self):
        self.password_input.fill(PASSWORD)
    def click_login(self):
        self.login_button.click()
        time.sleep(5)  # Wait for 5 seconds after clicking login

        print(USER_NAME)
        print(PASSWORD)
