from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    user_gender: str
    number: str
    day: str
    month: str
    year: str
    assert_data: str
    subject: str
    hobbies: str
    picture: str
    assert_picture: str
    address: str
    city: str
    state: str


user = User(
    first_name="Olga",
    last_name="Efimova",
    email="Oefi_Lefi@yandex.ru",
    user_gender="Female",
    number='9000000000',
    day='17',
    month='May',
    year='1999',
    assert_data='17 May,1999',
    subject='English',
    hobbies="Music",
    picture='pictures/snow_cat.png',
    assert_picture='snow_cat.png',
    address='Build, floor, flat',
    city='Delhi',
    state='NCR'
)
