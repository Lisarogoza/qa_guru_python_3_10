import allure
from demoqa_project.model.data.users_data import user
from demoqa_project.model.pages.practice_form import TestFormPage


@allure.title("Fill form successful")
def test_practice():
    user_olga = TestFormPage(user)
    with allure.step("Fill form"):
        user_olga.fill_form().submit()
    with allure.step("Assert results"):
        user_olga.assert_fields()

