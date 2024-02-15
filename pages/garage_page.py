from pages.base_page import BasePage
from pages.add_expenses_page import AddExpensesPage
from utils.locators import GaragePageLocators


class GaragePage(BasePage):
    def __init__(self, driver):
        self.locator = GaragePageLocators
        super().__init__(driver)

    def click_add_car(self):
        from pages.car_page import CarPage
        self.find_element(*self.locator.ADD_CAR).click()
        return CarPage(self.driver)

    def click_add_fuel_expense(self):
        self.find_element(*self.locator.ADD_FUEL_EXPENCE).click()
        return AddExpensesPage(self.driver)
