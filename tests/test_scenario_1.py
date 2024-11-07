from time import sleep
import allure

# @pytest.mark.order(2)
@allure.description("Test buy product 1")
def test_buy_product_1(driver):
    print("Start test 1")

    # Список с логинами

    login = Login_page(driver)
    login.authorization()


    print('Finish test 1')
    sleep(2)
