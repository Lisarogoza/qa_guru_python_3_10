import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1600
    browser.config.window_width = 1200

    yield
    browser.quit()
