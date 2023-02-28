from selene import have
from selene.support.shared import browser


class Gender:
    def __init__(self, locator, value):
        self.locator = locator
        self.value = value

    def gender(self):
        browser.all(self.locator).element_by(have.value(self.value)).element('..').click()
