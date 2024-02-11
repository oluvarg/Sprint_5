from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration(TestLocators):

    def test_creds_input_value_and_registry(self, random_name, random_password, random_email, driver):
        wait = WebDriverWait(driver, 5)
        driver.get('https://stellarburgers.nomoreparties.site/register')
        name = driver.find_element(*TestLocators.NAME_FOR_REG)
        name.send_keys(random_name)
        value_name = (driver.find_element(*TestLocators.NAME_FOR_REG).get_attribute('value'))

        assert value_name != '', 'Не удалось ввести данные в поле ввода "Имя"'

        email = driver.find_element(*TestLocators.EMAIL_FOR_REG)
        email.send_keys(random_email)
        value_email = driver.find_element(*TestLocators.EMAIL_FOR_REG).get_attribute('value')

        assert 'gmail.com' in value_email, 'Email не содержит gmail.com'

        password = driver.find_element(*TestLocators.PASSWORD_FOR_REG)
        password.send_keys(random_password)
        value_password = driver.find_element(*TestLocators.PASSWORD_FOR_REG).get_attribute('value')

        assert len(value_password) >= 6, 'Пароль меньше 6 символов'

        button = driver.find_element(*TestLocators.BUTT0N_FOR_REG)
        button.click()
        wait.until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_FOR_LOGIN))

        current_url_before_login = driver.current_url

        assert 'login' in current_url_before_login, 'Не удалось перейти на главную страницу при регистрации'

        driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(value_email)
        driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(value_password)
        driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()
        # time.sleep(2)

        current_url_after_login = driver.current_url

        assert 'stellarburgers.nomoreparties.site' in current_url_after_login, ('Не удалось войти недавно '
                                                                                'зарегистрированному пользователю')

        driver.find_element(*TestLocators.BUTTON_PROFILE).click()
        wait.until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT))
        login_name = driver.find_element(*TestLocators.PROFILE_NAME).get_attribute('value')

        driver.quit()

        assert login_name == random_name, 'Имя не соответствует имени при регистрации'

    def test_password_validation_negative(self, random_name, random_wrong_password, random_email, driver):
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
        driver.quit()

        assert 'login' not in current_url_before_login, 'Удачная регистрация с паролем < 6 символов'
