from pages.base_page import BasePage
from pages.login_page import LoginPage
from config.config import BASE_URL
from pages.forgotpassword_page import Forget_Password

def test_forgetpassword(browser_page):
    Page = browser_page
    login_page = LoginPage(Page)
    forget_password = Forget_Password(Page)

    login_page.navigate(BASE_URL)
    forget_password.forget_pass_click()
    forget_password.insert_email()
    forget_password.click_send_otp_button()

    # input("Wait and enter OTP, then press Enter to continue...")

    # forget_password.verify_otp()


