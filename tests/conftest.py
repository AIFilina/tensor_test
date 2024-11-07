import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    print("Driver open")
    options = webdriver.ChromeOptions()
    # Автоматическое закрытие окна
    options.add_experimental_option("detach", False)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print("Driver close")


# noinspection PyTypeChecker
@pytest.fixture(scope="module")
def set_group():
    print("enter system")
    yield
    print("exit system")