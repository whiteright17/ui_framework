from pages.base_page import BasePage
from utils.locators import AddCarPageLocators
from utils.utils import get_mileage


class CarPage(BasePage):
    def __init__(self, driver):
        self.locator = AddCarPageLocators
        super().__init__(driver)

    def click_brand_car(self):
        self.find_element(*self.locator.CAR_BRAND).click()
        return CarPage(self.driver)

    def change_porsche_car(self):
        self.find_element(*self.locator.PORSCHE).click()
        return CarPage(self.driver)

    def click_model_car(self):
        self.find_element(*self.locator.CAR_MODEL).click()
        return CarPage(self.driver)

    def change_model_car(self):
        self.find_element(*self.locator.PANAMERA).click()
        return CarPage(self.driver)

    def click_mileage_car(self):
        self.find_element(*self.locator.CAR_MILEAGE).send_keys(get_mileage())
        return CarPage(self.driver)

    def click_add_car_button(self):
        from pages.garage_page import GaragePage
        self.find_element(*self.locator.ADD_CAR_BUTTON).click()
        return GaragePage(self.driver)
