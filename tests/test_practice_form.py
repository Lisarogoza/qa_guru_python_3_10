import allure
from selene import browser

from demoqa_project.model.data.users_data import user
from demoqa_project.model.pages.practice_form import TestFormPage
from tests.utils import attach


@allure.title("Fill form successful")
def test_practice():
    user_olga = TestFormPage(user)
    with allure.step("Fill form"):
        user_olga.fill_form().submit()
    with allure.step("Assert results"):
        user_olga.assert_fields()

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
