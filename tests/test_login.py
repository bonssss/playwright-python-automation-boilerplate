from pages.login_page import LoginPage
from config.config import BASE_URL
def test_login(browser_page):
    page = browser_page

    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.enter_phone()
    login_page.enter_password()
    login_page.click_login()
    print()

    print("logged in")

   

    # Optional: verify successful login
    # assert "Dashboard" in page.title()
