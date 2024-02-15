from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage


class TestSignInPage:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def teardown_method(self):
        self.driver.quit()

    def test_page_load(self):
        page = HomePage(self.driver)
        assert page.check_if_loaded() is True

    def test_register_user(self):
        page = HomePage(self.driver)
        page = page.click_sign_up_button()
        page = page.register_with_valid_user("validuser")
        assert (page.find_element(By.XPATH, "//h1[text()='Garage']")
                .is_displayed())

    def test_add_car(self):
        page = HomePage(self.driver)
        page = page.click_sign_in_button()
        page = page.login()
        page = page.click_add_car()
        page = page.click_brand_car()
        page = page.change_porsche_car()
        page = page.click_model_car()
        page = page.change_model_car()
        page = page.click_mileage_car()
        page = page.click_add_car_button()
        assert (page.find_element(By.XPATH, "//h1[text()='Garage']")
                .is_displayed())

    def test_add_expenses(self):
        page = HomePage(self.driver)
        page = page.click_sign_in_button()
        page = page.login()
        page = page.click_add_fuel_expense()
        page = page.change_mileage()
        page = page.enter_number_of_liters()
        page = page.enter_total_cost()
        page = page.click_add_expenses()
        assert (page.find_element(By.XPATH, "//h1[text()='Fuel expenses']")
                .is_displayed())
