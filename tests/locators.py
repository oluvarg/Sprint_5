from selenium.webdriver.common.by import By


class TestLocators:

    # поле ввода имени на странице регистрации
    NAME_FOR_REG = By.XPATH, './/input[@name = "name"]'

    # поле ввода email на странице регистрации
    EMAIL_FOR_REG = By.XPATH, './/fieldset[2]/div/div/input[@name = "name"]'

    # поле ввода пароля на странице регистрации
    PASSWORD_FOR_REG = By.XPATH, './/input[@name  = "Пароль"]'

    # кнопка Зарегистрироваться
    BUTT0N_FOR_REG = By.XPATH, './/button[text() = "Зарегистрироваться"]'

    # поле ввода email на странице авторизации
    EMAIL_FOR_LOGIN = By.XPATH, './/input[@name = "name"]'

    # поле ввода пароля на странице авторизации
    PASSWORD_FOR_LOGIN = By.XPATH, './/input[@name  = "Пароль"]'

    # кнопка Войти
    BUTTON_FOR_LOGIN = By.XPATH, './/button[text() = "Войти"]'

    # тултип при некорректных данных введенного пароля на странице регистрации
    ERROR_VALIDATION_PASSWORD = By.XPATH, './/p[text() = "Некорректный пароль"]'

    # имя в личном кабинете
    PROFILE_NAME = By.XPATH, ('.//input[@class ="text input__textfield text_type_main-default '
                              'input__textfield-disabled"]')

    # кнопка Личный кабинет
    BUTTON_PROFILE = By.XPATH, './/a[@href = "/account"]'

    # кнопка Войти в аккаунт на главной странице
    BUTTON_LOGIN_MAIN_PAGE = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # кнопка Войти на странице регистрации
    BUTTON_LOGIN_IN_REG = By.XPATH, './/a[@href="/login"]'

    # кнопка восстановления пароля
    BUTTON_RECOVERY = By.XPATH, './/a[@href="/forgot-password"]'

    # поле ввода для email на 1-й странице восстановления пароля
    EMAIL_FOR_RECOVERY = By.XPATH, './/input[@name = "name"]'

    # кнопка восстановить на 1-й странице восстановления пароля
    BUTTON_FOR_RECOVERY = By.XPATH, './/button[ text() = "Восстановить"]'

    # кнопка Войти на 1-й странице восстановления пароля
    BUTTON_LOGIN_FOR_RECOVERY = By.XPATH, './/a[text() = "Войти"]'

    # кнопка Выйти на странице профиля
    BUTTON_EXIT = By.XPATH, ".//button[text() = 'Выход']"

    # кнопка конструктор
    BUTTON_CONSTRUCTOR = By.XPATH, './/p[text() = "Конструктор"]'

    # кнопка Оформить заказ
    BUTTON_CHECKOUT = By.XPATH, './/button[text() = "Оформить заказ"]'

    # поле ввода пароля на странице восстановления пароля
    PASSWORD_FOR_RESET = By.XPATH, './/input[@type = "password"]'

    # кнопка Начинки
    FILINGS_BUTTON = By.XPATH, './/span[text() = "Начинки"]'

    # наименование раздела Начинки
    FILINGS_CONTENT = By.XPATH, './/h2[text() = "Начинки"]'

    # кнопка Соусы
    SAUCES_BUTTON = By.XPATH, './/span[text() = "Соусы"]'

    # наименование раздела Соусы
    SAUCES_CONTENT = By.XPATH, './/h2[text() = "Соусы"]'

    # кнопка Булки
    BUNS_BUTTON = By.XPATH, './/span[text() = "Булки"]'

    # наименование раздела Булки
    BUNS_CONTENT = By.XPATH, './/h2[text() = "Булки"]'
