from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope='class')
def browser():
    """
     Инициализирует новый экземпляр WebDriver для браузера Google Chrome перед тем, как начать выполнение тестового
     класса и осуществляет его закрытие после выполнения всех тестов в классе.
     Использует ChromeDriverManager для автоматической установки необходимой версии драйвера.

    :yield: Итератор возвращающий экземпляр WebDriver для использования в тестах.
    """
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()