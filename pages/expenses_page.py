from pages.base_page import BasePage
from utils.locators import ExpensesPageLocators


class ExpensesPage(BasePage):
    def __init__(self, driver):
        self.locator = ExpensesPageLocators
        super().__init__(driver)
