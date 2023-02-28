from selene import have
from selene.support.shared import browser


class Dropdown:
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def choose_option(self):
        browser.element(self.locator).click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(self.text)).click()
