from base.base_class import Base


class About_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #locators

    working ="//h2[text()='Работаем']"
    pic1 = '//img[@alt="Разрабатываем систему СБИС"]'
    pic2 = '//img[@alt="Продвигаем сервисы"]'
    pic3 = '//img[@alt="Создаем инфраструктуру"]'
    pic4 = '//img[@alt="Сопровождаем клиентов"]'

    '''Method check banner РАБОТАЕМ'''

    def check_working(self):
        self.scroll_to_element(self.working)
        self.assert_word(self.working,'Работаем')
        print('There is banner РАБОТАЕМ')

    '''Method check size pictures for banner РАБОТАЕМ'''

    def check_size_working_pic(self):
        images = [self.find_by_xpath(self.pic1),
                  self.find_by_xpath(self.pic2),
                  self.find_by_xpath(self.pic3),
                  self.find_by_xpath(self.pic4),]

        first_image_size = images[0].size

        # Сравниваем размеры остальных изображений с первым
        for img in images[1:]:
            image_size = img.size
            assert image_size['width'] == first_image_size[
                'width'], f"Width mismatch for image {img}. Expected {first_image_size['width']}, but got {image_size['width']}"
            assert image_size['height'] == first_image_size[
                'height'], f"Height mismatch for image {img}. Expected {first_image_size['height']}, but got {image_size['height']}"

        print("Все изображения имеют одинаковые размеры.")



