from playwright.sync_api import Page
from pages.base_page import BasePage
from config.config import USER_NAME


import time
import re
class Forget_Password(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)

        self.forget_password_button = page.get_by_role("link")
        self.enter_email = page.get_by_role("textbox")
        self.send_otp_button = page.get_by_role("button", name=re.compile(r"Send OTP", re.IGNORECASE))
        self
    def forget_pass_click(self):
        self.forget_password_button.click()
        time.sleep(5)
    def insert_email(self):
        self.enter_email.fill(USER_NAME)
    def click_send_otp_button(self):
        self.send_otp_button.click()

    
