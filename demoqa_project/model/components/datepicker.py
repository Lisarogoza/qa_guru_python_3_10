from selene import have
from selene.support.shared import browser


class Birthday:
    def __init__(self, locator, value):
        self.locator = locator
        self.value = value

    def select_date(self):
        browser.element(self.locator).all('option').element_by(have.exact_text(self.value)).click()
