from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSection:

    def test_fillings(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*TestLocators.FILINGS_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FILINGS_CONTENT))

        name_fillings = driver.find_element(*TestLocators.FILINGS_CONTENT)

        assert 'Начинки' in name_fillings.text, 'Не удалось перейти в раздел "Начинки"'

    def test_sauces(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*TestLocators.SAUCES_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SAUCES_CONTENT))

        name_sauces = driver.find_element(*TestLocators.SAUCES_CONTENT)

        assert 'Соусы' in name_sauces.text, 'Не удалось перейти в раздел "Соусы"'

    def test_buns(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        driver.find_element(*TestLocators.FILINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.FILINGS_CONTENT))

        driver.find_element(*TestLocators.BUNS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUNS_CONTENT))

        name_buns = driver.find_element(*TestLocators.BUNS_CONTENT)

        assert 'Булки' in name_buns.text, 'Не удалось перейти в раздел "Булки"'
