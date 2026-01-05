import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Инициализация:
@pytest.fixture
def driver():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Тестирование успешной авторизации:
@allure.title("Успешная авторизация с валидными данными")
@allure.description("Тестирование успешной авторизации с валидными данными")
def test_successful_login(driver):
    """
    Тестирование успешной авторизации на сайте The Internet HerokuApp
    Шаги:
    1. Открываем страницу с формой.
    2. Заполняем текстовое поле верным логином.
    3. Заполняем поле верным паролем.
    4. Отправляем форму.
    5. Проверяем сообщение об успешной авторизации.
    """
# 1. Открываем страницу с формой:
    driver.get("https://the-internet.herokuapp.com/login")

# 2. Заполняем текстовое поле:
    username_field = driver.find_element(By.NAME, "username")
    username_field.clear()
    username_field.send_keys("tomsmith")
# 3. Заполняем поле пароля:
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("SuperSecretPassword!")

# 4. Отправляем форму:
    login_button = driver.find_element(By.CSS_SELECTOR, ".radius")
    login_button.click()

# 5. Проверка сообщения об успешной авторизации:
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
    )
    assert "You logged into a secure area!" in success_message.text.strip(), \
           "Ошибка: Сообщение об успешной авторизации отсутствует."

# Тестирование неуспешной авторизации:
@allure.title("Неуспешная авторизация")
@allure.description("Тестирование неуспешной авторизации на сайте The Internet HerokuApp")
def test_failed_login(driver):
    """
    Тестирование неуспешной авторизации на сайте The Internet HerokuApp
    Шаги:
    1. Открываем страницу с формой.
    2. Заполняем текстовое поле неверным логином.
    3. Заполняем поле неверным паролем.
    4. Отправляем форму.
    5. Проверяем сообщение об ошибке.
    """
# 1. Открываем страницу с формой:
    driver.get("https://the-internet.herokuapp.com/login")

# 2. Заполняем текстовое поле:
    username_field = driver.find_element(By.NAME, "username")
    username_field.clear()
    username_field.send_keys("wrong_user")
# 3. Заполняем поле пароля:
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("wrong_password")

# 4. Отправляем форму:
    login_button = driver.find_element(By.CSS_SELECTOR, ".radius")
    login_button.click()

# 5. Проверка сообщения об ошибке:
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "flash.error"))
    )
    assert "Your username is invalid!" in error_message.text.strip(), \
           "Ошибка: Сообщение об ошибочной авторизации отсутствует."

