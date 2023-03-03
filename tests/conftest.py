import pytest
from selene.support.shared import browser
from tests.utils import attach

@pytest.fixture(autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1600
    browser.config.window_width = 1200

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
