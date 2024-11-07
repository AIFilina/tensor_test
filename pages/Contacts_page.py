# import allure

from base.base_class import Base

class Contacts_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #locators
    banner_tensor = "//div[contains(@class,'sbisru-Contacts__border-left--border-xm')]//a[@title='tensor.ru']"
    location = "(//span[contains(@class,'sbis_ru-Region-Chooser__text')])[1]"

    partner_16 = '//div[@title="СБИС - Казань"]'
    partner_41 = '//div[@title="СБИС - Камчатка"]'

    region_41 ='//span[@title="Камчатский край"]'

    '''Method click by banner ТЕНЗОР'''

    def click_banner_tensor(self):
        self.click_button(self.banner_tensor)
        print('Нажат БАНЕР ТЕНЗОР')

    '''Methods check regions '''

    def check_region_16(self):
        self.assert_word(self.location,'Республика Татарстан')

    def check_region_41(self):
        self.assert_word(self.location,'Камчатский край')

    '''Methods check partners '''

    def check_partner_16(self):
        element = self.find_by_xpath(self.partner_16)
        print(f'There is a partner {element.text}')

    def check_partner_41(self):
        element = self.find_by_xpath(self.partner_41)
        print(f'There is a partner {element.text}')

    '''Method change region by КАМЧАТСКИЙ КРАЙ(41)'''

    def change_region(self):
        self.click_button(self.location)
        self.click_button(self.region_41)
        print('Регион изменен на Камчатский край')



