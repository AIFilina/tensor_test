from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #locators
    contacts = "//div[text()='Контакты']"
    contacts_2 = "//span[text()='Еще 841 офис в России']"

    downloads="/a[text()='Скачать локальные версии']"
    web_install = '//div[@class="sbis_ru-DownloadNew-loadLink"]//a[text()="Скачать (Exe 11.48 МБ) "]'


    def click_contacts(self):
        self.click_button(self.contacts)
        print('Нажата кнопка КОНТАКТЫ')

    def click_all_office(self):
        self.click_button(self.contacts_2)
        print('Нажата кнопка "Еще 841 офис в России"')

    def click_downloads(self):
        self.click_button(self.downloads)
        print('Нажата кнопка СКАЧАТЬ ЛОКАЛЬНЫЕ ВЕРСИИ')

