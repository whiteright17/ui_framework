from pages.base_page import BasePage
from utils.locators import AddExpensesPageLocators
from utils.utils import change_mileage


class AddExpensesPage(BasePage):
    def __init__(self, driver):
        self.locator = AddExpensesPageLocators
        super().__init__(driver)

    def change_mileage(self):
        self.find_element(*self.locator.EDIT_MILEAGE).clear()
        self.find_element(*self.locator.EDIT_MILEAGE).send_keys(change_mileage())
        return AddExpensesPage(self.driver)

    def enter_number_of_liters(self):
        self.find_element(*self.locator.NUMBER_LITERS).send_keys('10')
        return AddExpensesPage(self.driver)

    def enter_total_cost(self):
        self.find_element(*self.locator.TOTAL_COST).send_keys('3.50')
        return AddExpensesPage(self.driver)

    def click_add_expenses(self):
        from pages.expenses_page import ExpensesPage
        self.find_element(*self.locator.ADD_EXPENSE_BUTTON).click()
        return ExpensesPage(self.driver)
