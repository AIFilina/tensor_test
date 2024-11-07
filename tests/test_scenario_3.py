from time import sleep
import allure

from pages.Download_page import Download_page
from pages.Main_page import Main_page

from utilites.logger import Logger


@allure.description("Сценарий 2")
def test_scenario_3(driver):
    print('Scenario 3 start')
    Logger.add_start_step('Scenario 3 start')

    url_sbis = 'https://sbis.ru/'
    url_download ='https://sbis.ru/download/'

    main = Main_page(driver)
    download = Download_page(driver)

    main.open_url(url_sbis)

    main.scroll_to_download()
    main.click_downloads()

    download.assert_url(url_download)
    download.click_web_install()

    download.check_file_in_path()
    download.check_size_download()

    Logger.add_end_step(driver.current_url,"Scenario 3 end")
    print('Scenario 3 end')
    sleep(10)
