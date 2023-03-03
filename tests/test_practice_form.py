import allure
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa_project.model.data.users_data import user
from demoqa_project.model.pages.practice_form import TestFormPage



@allure.title("Fill form successful")
def test_practice():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver

    user_olga = TestFormPage(user)
    with allure.step("Fill form"):
        user_olga.fill_form().submit()
    with allure.step("Assert results"):
        user_olga.assert_fields()
