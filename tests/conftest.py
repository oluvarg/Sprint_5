import pytest

from helpers import (helper_name,
                     helper_email,
                     helper_password)
from locators import TestLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def user_creds(driver):

    random_name = helper_name()
    random_password = helper_password()
    random_email = helper_email()

    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(*TestLocators.NAME_FOR_REG).send_keys(random_name)
    driver.find_element(*TestLocators.EMAIL_FOR_REG).send_keys(random_email)
    driver.find_element(*TestLocators.PASSWORD_FOR_REG).send_keys(random_password)
    driver.find_element(*TestLocators.BUTT0N_FOR_REG).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        TestLocators.BUTTON_FOR_LOGIN))

    user_creds = [random_name, random_email, random_password]

    return user_creds


@pytest.fixture
def login_user(driver, user_creds):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*TestLocators.EMAIL_FOR_LOGIN).send_keys(user_creds[1])
    driver.find_element(*TestLocators.PASSWORD_FOR_LOGIN).send_keys(user_creds[2])
    driver.find_element(*TestLocators.BUTTON_FOR_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        TestLocators.BUTTON_CHECKOUT))


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
