from helpers import (helper_name,
                     helper_email,
                     helper_password,
                     helper_wrong_password)
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_and_login_new_user(self, driver):

        random_name = helper_name()
        random_password = helper_password()
        random_email = helper_email()

        wait = WebDriverWait(driver, 5)
        driver.get('https://stellarburgers.nomoreparties.site/register')
        name = driver.find_element(*TestLocators.NAME_FOR_REG)
        name.send_keys(random_name)

        email = driver.find_element(*TestLocators.EMAIL_FOR_REG)
        email.send_keys(random_email)
        value_email = driver.find_element(*TestLocators.EMAIL_FOR_REG).get_attribute('value')

        password = driver.find_element(*TestLocators.PASSWORD_FOR_REG)
        password.send_keys(random_password)
        value_password = driver.find_element(*TestLocators.PASSWORD_FOR_REG).get_attribute('value')

        button = driver.find_element(*TestLocators.BUTT0N_FOR_REG)
        button.click()
        wait.until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_FOR_LOGIN))

        driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(value_email)
        driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(value_password)
        driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()
        wait.until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_CHECKOUT))
        driver.find_element(*TestLocators.BUTTON_PROFILE).click()
        wait.until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT))

        current_url_after_login = driver.current_url

        assert '/account/profile' in current_url_after_login, ('Не удалось зарегестироваться и войти недавно '
                                                               'зарегестрированному пользователю')

    def test_password_validation_negative(self, driver):
        random_name = helper_name()
        random_email = helper_email()
        random_wrong_password = helper_wrong_password()

        driver.get('https://stellarburgers.nomoreparties.site/register')

        name = driver.find_element(*TestLocators.NAME_FOR_REG)
        name.send_keys(random_name)
        email = driver.find_element(*TestLocators.EMAIL_FOR_REG)
        email.send_keys(random_email)
        password = driver.find_element(*TestLocators.PASSWORD_FOR_REG)
        password.send_keys(random_wrong_password)

        button = driver.find_element(*TestLocators.BUTT0N_FOR_REG)
        button.click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            TestLocators.ERROR_VALIDATION_PASSWORD))

        current_url_before_login = driver.current_url

        assert 'login' not in current_url_before_login, 'Удачная регистрация с паролем < 6 символов'
