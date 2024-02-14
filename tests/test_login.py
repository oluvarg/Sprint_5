from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_login_main_paige(self, driver, user_creds):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.BUTTON_LOGIN_MAIN_PAGE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_FOR_LOGIN))

        driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(user_creds[1])
        driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(user_creds[2])
        driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CHECKOUT))

        driver.find_element(*TestLocators.BUTTON_PROFILE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_EXIT))
        current_profile_url = driver.current_url

        assert '/account/profile' in current_profile_url, 'Не удалось авторизоваться'

    def test_login_profile(self, driver, user_creds):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.BUTTON_PROFILE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_FOR_LOGIN))

        driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(user_creds[1])
        driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(user_creds[2])
        driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Не удалось авторизоваться'

    def test_login_registration(self, driver, user_creds):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_REG).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.EMAIL_FOR_LOGIN))

        driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(user_creds[1])
        driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(user_creds[2])
        driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Не удалось авторизоваться'

    def test_login_recovery_password(self, driver, user_creds):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*TestLocators.BUTTON_LOGIN_FOR_RECOVERY).click()

        driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(user_creds[1])
        driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(user_creds[2])
        driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Не удалось авторизоваться'

    def test_login_reset_password(self, driver, user_creds):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.EMAIL_FOR_RECOVERY))

        driver.find_element(*TestLocators.EMAIL_FOR_RECOVERY).send_keys(user_creds[1])
        driver.find_element(*TestLocators.BUTTON_FOR_RECOVERY).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            TestLocators.PASSWORD_FOR_RESET))

        driver.find_element(*TestLocators.BUTTON_LOGIN_FOR_RECOVERY).click()

        driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(user_creds[1])
        driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(user_creds[2])
        driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Неверные креды'
