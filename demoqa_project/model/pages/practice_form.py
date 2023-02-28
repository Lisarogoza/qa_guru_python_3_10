from selene.support.shared import browser
from selene import have
from demoqa_project.model.components.checkbox import Hobby
from demoqa_project.model.components.datepicker import Birthday
from demoqa_project.model.components.dropdown import Dropdown
from demoqa_project.model.components.radiobutton import Gender
from demoqa_project.utils import file_path, scroll


class TestFormPage:
    def __init__(self, person):
        self.person = person

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def fill_form(self):
        browser.open('/automation-practice-form')
        browser.element('#firstName').type(self.person.first_name)

        browser.element('#lastName').type(self.person.last_name)

        browser.element('#userEmail').type(self.person.email)
        user_gender = Gender('[name=gender]', self.person.user_gender)
        user_gender.gender()
        browser.element('#userNumber').type(self.person.number)

        browser.element('#dateOfBirthInput').click()

        browser.element('.react-datepicker__month-select').click()
        month = Birthday('.react-datepicker__month-select', self.person.month)
        month.select_date()

        browser.element('.react-datepicker__year-select').click()
        year = Birthday('.react-datepicker__year-select', self.person.year)
        year.select_date()

        browser.element(f'.react-datepicker__day--0{self.person.day}').click()

        browser.element('#subjectsInput').type(self.person.subject).press_enter()

        user_hobby = Hobby('[for^=hobbies-checkbox]', self.person.hobbies)
        user_hobby.hobby()

        scroll.scroll_to('#currentAddress')

        browser.element('#currentAddress').type(self.person.address)

        file_path.create_file_path('#uploadPicture', self.person.picture)

        state = Dropdown('#state', self.person.state)
        state.choose_option()

        city = Dropdown('#city', self.person.city)
        city.choose_option()
        return self

    def assert_fields(self):
        browser.element('.table').all('td').even.should(have.texts(
            self.person.first_name + ' ' + self.person.last_name,
            self.person.email,
            self.person.user_gender,
            self.person.number,
            self.person.assert_data,
            self.person.subject,
            self.person.hobbies,
            self.person.assert_picture,
            self.person.address,
            self.person.state + ' ' + self.person.city

        ))
        return self
