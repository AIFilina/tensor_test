from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #locators
    contacts = "//div[text()='Контакты']"
    contacts_2 = "//span[text()='Еще 841 офис в России']"

    downloads="//a[text()='Скачать локальные версии']"

    '''Method click by button КОНТАКТЫ'''

    def click_contacts(self):
        self.click_button(self.contacts)
        print('Нажата кнопка КОНТАКТЫ')

    '''Method click by "Еще 841 офис в России"'''

    def click_all_office(self):
        self.click_button(self.contacts_2)
        print('Нажата кнопка "Еще 841 офис в России"')

    '''Method click by СКАЧАТЬ ЛОКАЛЬНЫЕ ВЕРСИИ'''

    def click_downloads(self):
        self.click_button(self.downloads)
        print('Нажата кнопка СКАЧАТЬ ЛОКАЛЬНЫЕ ВЕРСИИ')

    '''Method scroll by element'''

    def scroll_to_download(self):
        self.scroll_to_element(self.downloads)
