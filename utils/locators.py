from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO = (By.XPATH, "//a[@class='header_logo']")
    SIGNUP = (By.XPATH, "//button[text()='Sign up']")
    SIGNIN = (By.XPATH, "//button[contains(@class, 'header_signin')]")


class LoginPageLocators(object):
    EMAIL = (By.ID, "signinEmail")
    PASSWORD = (By.ID, "signinPassword")
    LOGIN = (By.XPATH, "//button[text()='Login']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class SignupPageLocators(object):
    NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    REGISTER = (By.XPATH, "//button[text()='Register']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class GaragePageLocators(object):
    ADD_CAR = (By.XPATH, "//button[text()='Add car']")
    ADD_FUEL_EXPENCE = (By.XPATH, "//button[text()='Add fuel expense']")


class AddCarPageLocators(object):
    CAR_BRAND = (By.ID, "addCarBrand")
    PORSCHE = (By.XPATH, "//option[text()='Porsche']")
    CAR_MODEL = (By.ID, "addCarModel")
    PANAMERA = (By.XPATH, "//option[text()='Panamera']")
    CAR_MILEAGE = (By.ID, "addCarMileage")
    ADD_CAR_BUTTON = (By.XPATH, "//button[text()='Add']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
class ExpensesPageLocators(object):
    ADD_EXPENSE = (By.XPATH, "//button[text()='Add an expense']")
    EDIT_EXPENSE = (By.CSS_SELECTOR, "btn btn-edit")
    DELETE_EXPENSE = (By.CSS_SELECTOR, "btn btn-delete")

class AddExpensesPageLocators(object):
    EDIT_MILEAGE = (By.ID, "addExpenseMileage")
    NUMBER_LITERS = (By.ID, "addExpenseLiters")
    TOTAL_COST = (By.ID, "addExpenseTotalCost")
    ADD_EXPENSE_BUTTON = (By.XPATH, "//button[text()='Add']")
    CANCEL_EXPENSE_BUTTON = (By.XPATH, "//button[text()='Cancel']")