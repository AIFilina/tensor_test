from base.base_class import Base


class Main_page(Base):

    #locators
    contacts = "//div[text()='Контакты']"
    contacts_2 = "//span[text()='Еще 841 офис в России']"

    def click_contacts(self):
        self.click_button(self.contacts)
        print('Нажата кнопка КОНТАКТЫ')

    def click_all_office(self):
        self.click_button(self.contacts_2)
        print('Нажата кнопка "Еще 841 офис в России"')

