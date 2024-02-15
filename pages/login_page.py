from pages.base_page import BasePage
from pages.garage_page import GaragePage
from utils.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver, user_for_login):
        self.locator = LoginPageLocators
        self.user_for_login = user_for_login
        super().__init__(driver)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.LOGIN).click()

    def login(self):
        user = self.user_for_login
        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.click_login_button()
        return GaragePage(self.driver)

    def login_with_valid_user(self):
        self.login()
        return GaragePage(self.driver)

    def login_with_in_valid_user(self, ):
        self.login()
        return self.find_element(*self.locator.ERROR_MESSAGE).text
