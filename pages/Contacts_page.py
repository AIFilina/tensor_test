import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Contacts_page(Base):

    # URL

    url_sbis = 'https://sbis.ru/'
    url_tensor = 'https://tensor.ru/'

    #locators

    contacts= "//div[text()='Контакты']"
    # sila_v_lud ="//p[text()='Сила в людях']"
    # more_detalies = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
    # working ="//h2[text()='Работаем']"
    # pic1 = '//img[@alt="Разрабатываем систему СБИС"]'
    # pic2 = '//img[@alt="Продвигаем сервисы"]'
    # pic3 = '//img[@alt="Создаем инфраструктуру"]'
    # pic4 = '//img[@alt="Сопровождаем клиентов"]'

    #getters



    #actions

    def click_contacts_button(self):
        self.get_contacts().click()
        print('Нажата кнопка КОНТАКТЫ')

    #Methods

    def
