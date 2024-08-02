import os

from selene import browser, have


def test_demoqa ():

    browser.open('/')
    browser.element('#firstName').type('Sosha')
    browser.element('#lastName').type('Hex')
    browser.element('#userEmail').type('sinterma@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('0987890690')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="0"]').click()
    browser.element('.react-datepicker__year-select option[value="1991"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--003').click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.png'))
    browser.element('#currentAddress').type('Germany')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').click()
    browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
"Sosha Hex",
        "sinterma@gmail.com",
        "Other",
        "0987890690",
        "03 January,1991",
        "English",
        "Music",
        "picture.png",
        "Germany",
        "NCR Delhi",
    )
    )
