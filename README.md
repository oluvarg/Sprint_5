# Sprint_5

## Описание:
В данном проекты содержатся тесты, покрывающие часть фунциональности сайта https://stellarburgers.nomoreparties.site/.

### Содержимое проекты

* Директория tests:
  * `test_registration.py` - проверка успешной регистрации и валидации поля "Пароль"
  * `test_login.py` - проверка перехода из разных положений на страницу авторизации и авторизация
  * `test_jump_some_page` - проверка перехода на различные страницы сайты
  * `test_section.py` - проверка перехода в разделы "Начинки", "Соусы", "Булки"
  * `helpers.py` - хелперы генерирующие креды
  * `locators.py` - локаторы
  * `conftest.py` - фикстуры

### Запуск тестов:

`pytest .\tests\test_jump_some_page.py, .\tests\test_login.py, .\tests\test_registration.py, .\tests\test_sections.py`