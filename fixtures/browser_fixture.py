import pytest
from playwright.sync_api import sync_playwright
from config.config import Config


@pytest.fixture(scope="function")
def browser_page():

    with sync_playwright() as p:

        if Config.BROWSER == "chromium":
            browser = p.chromium.launch(headless=Config.HEADLESS)

        elif Config.BROWSER == "firefox":
            browser = p.firefox.launch(headless=Config.HEADLESS)

        else:
            browser = p.webkit.launch(headless=Config.HEADLESS)

        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()
