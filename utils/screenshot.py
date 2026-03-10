import os

def take_screenshot(page):
    path = os.path.join("reports", "screenshots", "failed_test.png")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    page.screenshot(path=path)
    print(f"Screenshot saved: {path}")
