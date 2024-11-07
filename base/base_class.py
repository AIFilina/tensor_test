
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains

from tests.conftest import driver
from utilites.logger import Logger


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    '''Method find_element'''

    def find_by_xpath(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, locator)))

    '''Method click button'''

    def click_button(self,locator):
        try:
            element =  WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, locator)))
            element.click()
        except TimeoutException as e:
            print(f"TimeoutException: Element with locator {locator} is not clickable after 20 seconds.")
            Logger.log_error(e)

    '''Method scroll by element'''

    def scroll_to_element(self,locator):
        try:
            element =  WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            print(f"Move to element with locator: {locator}")
        except TimeoutException as e:
            print(f"TimeoutException: Element with locator {locator} is not clickable after 20 seconds.")
            Logger.log_error(e)
        except Exception as e:
            # Логируем любую другую ошибку
            print(f"An error occurred while scrolling to element with locator {locator}.")
            Logger.log_error(f"Error: {str(e)}")

    """Method get current url"""

    def get_current_url(self):
        try:
            get_url = self.driver.current_url
            print("Current url: " + get_url)
        except WebDriverException as e:
            print(f"Error getting current URL: {str(e)}")
            Logger.log_error(e)

    """Method open url"""

    def open_url(self,url):
        try:
            self.driver.get(url)
            print("Open: " + url)
        except WebDriverException as e:
            print(f"Error open URL: {str(e)}")
            Logger.log_error(e)

    """Method assert word"""

    def assert_word(self,word_locator:str, result):
        try:
            word =  WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, word_locator)))
            value_word = word.text
            assert value_word == result, f"Expected '{result}', but got '{value_word}'"
            print(f"Good value: {result}")
        except AssertionError as e:
            print(f"Assertion Error: {str(e)}")
            Logger.log_error(e)
        except NoSuchElementException as e:
            print(f"Error: Element not found: {str(e)}")
            Logger.log_error(e)


    """Method assert url"""

    def assert_url(self, result):
        try:
            get_url = self.driver.current_url
            assert get_url == result, f"Expected URL '{result}', but got '{get_url}'"
            print("Good value URL")
        except AssertionError as e:
            print(f"Assertion Error: {str(e)}")
            Logger.log_error(e)
        except WebDriverException as e:
            print(f"Error getting current URL: {str(e)}")
            Logger.log_error(e)

    '''Method assert Title'''

    def assert_title(self,expected_title):
        try:
            assert expected_title.lower() in self.driver.title.lower()
            print(f"Заголовок содержит информацию о '{expected_title}'")
        except AssertionError as e:
            print(f"Заголовок не содержит информацию o '{expected_title}'")
            print(f"Assertion Error: {str(e)}")
            Logger.log_error(e)

    '''Method assert info in url'''

    def assert_info_in_url(self,expected_value):
        try:
            assert expected_value.lower() in self.driver.current_url.lower()
            print(f'URL содержит в себе подстроку {expected_value}')
        except AssertionError as e:
            print(f"URL не содержит информацию о '{expected_value}'")
            print(f"Assertion Error: {str(e)}")
            Logger.log_error(e)