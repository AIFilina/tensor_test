from time import sleep
import allure



from pages.Contacts_page import Contacts_page
from pages.Main_page import Main_page

from utilites.logger import Logger


@allure.description("Сценарий 2")

def test_scenario_2(driver):
    print('Scenario 2 start')
    Logger.add_start_step('Scenario 2 start')

    url_sbis = 'https://sbis.ru/'
    url_contacts = 'https://sbis.ru/contacts'

    main = Main_page(driver)
    contact = Contacts_page(driver)

    main.open_url(url_sbis)
    main.click_contacts()
    main.click_all_office()
    main.assert_url(url_contacts)

    contact.check_region_16()

    contact.check_partner_16()

    contact.change_region()

    sleep(2)

    contact.check_region_41()
    contact.assert_title('Камчатский край')
    contact.check_partner_41()

    contact.assert_info_in_url('41')

    Logger.add_end_step(driver.current_url,"Scenario 2 end")
    print('Scenario 2 end')
    sleep(2)
