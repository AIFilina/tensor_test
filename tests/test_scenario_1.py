from time import sleep
import pytest
import allure

from pages.About_page import About_page
from pages.Contacts_page import Contacts_page
from pages.Main_page import Main_page
from pages.Tensor_page import Tensor_page
from utilites.logger import Logger


@allure.description("Сценарий 1")
def test_scenario_1(driver):
    print('Scenario 1 start')
    Logger.add_start_step('Scenario 1 start')

    # uRL
    url_sbis = 'https://sbis.ru/'
    url_tensor = 'https://tensor.ru/'
    url_contacts = 'https://sbis.ru/contacts'
    url_about ='https://tensor.ru/about'

    #create objects
    main = Main_page(driver)
    contact = Contacts_page(driver)
    tensor =Tensor_page(driver)
    about = About_page(driver)


    main.open_url(url_sbis)
    main.click_contacts()
    main.click_all_office()
    main.assert_info_in_url(url_contacts)

    contact.click_banner_tensor()

    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[1])
    sleep(2)

    contact.assert_url(url_tensor)

    tensor.check_power_of_people()
    tensor.click_more_detalies()
    tensor.assert_url(url_about)

    about.check_working()
    about.check_size_working_pic()


    Logger.add_end_step(driver.current_url,"Scenario 1 end")
    print('Scenario 1 end')
    sleep(2)
