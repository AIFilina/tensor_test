from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
import os

class Download_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #locators
    web_install = '//div[@class="sbis_ru-DownloadNew-loadLink"]//a[text()="Скачать (Exe 11.48 МБ) "]'

    path_download1 = "C:\\Users\\ajnaf\\PycharmProjects\\tensor_test\\downloads\\"
    size_download1 = 11.48
    name_download1 = 'sbisplugin-setup-web.exe'
    file1 = os.path.join(path_download1, name_download1)

    '''Method click by " Скачать (Exe 11.48 МБ)"'''

    def click_web_install(self):
        self.click_button(self.web_install)
        print('Нажата кнопка Скачать (Exe 11.48 МБ) ')

    '''Method wait for exists file'''

    def check_file_in_path(self, timeout=60):
        # Ожидаем до 30 секунд появления файла в директории
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(lambda wait_condition: os.path.exists(self.file1))
            print('Файл успешно скачан')
        except TimeoutError as e:
            print(f"Assertion Error: {str(e)}")

    '''Method check size file'''

    def check_size_download(self):
        file_size = os.path.getsize(self.file1) / (1024 ** 2)
        try:
            print(f'{round(file_size, 2)}   {self.size_download1}')
            assert round(file_size, 2) == self.size_download1
            print('Размер файла соответствует ожидаемому')
        except AssertionError as e:
            print(f"Assertion Error: {str(e)}")

