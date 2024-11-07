import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  # Импортируем Service

@pytest.fixture(scope="module")
def driver():
    print("Driver open")
    options = webdriver.ChromeOptions()

    # Автоматическое закрытие окна
    options.add_experimental_option("detach", False)

    # Параметры для загрузки файлов
    options.add_experimental_option("prefs", {
        "download.default_directory": "C:\\Users\\ajnaf\\PycharmProjects\\tensor_test\\downloads\\",  # Путь для загрузок
        "download.prompt_for_download": False,  # Отключить запрос на подтверждение загрузки
        "download.directory_upgrade": True,  # Разрешить обновление пути загрузки
        "safebrowsing.enabled": True,  # Отключить безопасный просмотр
        "profile.default_content_settings.popups": 0,  # Отключить всплывающие окна
        "profile.default_content_setting_values.automatic_downloads": 1,  # Включить автоматическое скачивание
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,  # Разрешить скачивание всех файлов
    })

    # Создаем объект Service для указания пути к драйверу
    service = Service(ChromeDriverManager().install())

    # Запускаем браузер с переданными опциями и сервисом
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    print("Driver close")


# noinspection PyTypeChecker
@pytest.fixture(scope="module")
def set_group():
    print("enter system")
    yield
    print("exit system")