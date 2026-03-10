class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def fill(self, locator, value):
        locator.fill(value)
