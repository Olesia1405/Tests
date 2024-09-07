import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Установите путь к вашему ChromeDriver
CHROME_DRIVER_PATH = '/path/to/chromedriver'

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Запуск в фоновом режиме (без GUI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_yandex_login_success(driver):
    # Откройте страницу авторизации
    driver.get('https://passport.yandex.ru/auth/')

    # Найдите поля ввода и кнопку отправки
    username_field = driver.find_element(By.NAME, 'login')
    password_field = driver.find_element(By.NAME, 'passwd')
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button.passp-sign-in-button')

    # Введите учетные данные (замените на реальные для тестирования)
    username = 'your_username'
    password = 'your_password'

    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)

    # Ожидаем, что страница перейдет на страницу ввода пароля
    driver.implicitly_wait(5)  # Установите необходимое время ожидания

    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Ожидаем успешного входа (например, проверяем наличие элемента, который отображается после успешного входа)
    driver.implicitly_wait(10)  # Установите необходимое время ожидания
    try:
        # Пример: Проверяем наличие элемента после успешного входа
        profile_icon = driver.find_element(By.CSS_SELECTOR, '.user-menu__icon')
        assert profile_icon.is_displayed()
    except:
        pytest.fail("Не удалось выполнить вход или найти элемент после входа.")
