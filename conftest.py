import sys
import os
import pytest
from utils.screenshot import take_screenshot

# Fix import path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from playwright.sync_api import sync_playwright

# Browser fixture
@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        headless = True if os.getenv("CI") else False
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("browser_page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            take_screenshot(page)
