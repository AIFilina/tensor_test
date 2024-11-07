from base.base_class import Base


class Tensor_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #locators
    power_of_people ="//p[text()='Сила в людях']"
    more_detalies = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'

    '''Check banner СИЛА В ЛЮДЯХ'''

    def check_power_of_people(self):
        self.scroll_to_element(self.power_of_people)
        self.assert_word(self.power_of_people,'Сила в людях')

    '''Method click by ПОДРОБНЕЕ'''

    def click_more_detalies(self):
        self.click_button(self.more_detalies)
        print('Нажата кнопка ПОДРОБНЕЕ')


