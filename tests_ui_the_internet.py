from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

URL = "https://the-internet.herokuapp.com/"


class TestTheInternetWebsite:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_open_url(self):
        self.driver.get(URL)
        assert self.driver.title == 'The Internet'

    def test_check_checkboxes(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/checkboxes']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Checkboxes'
        checkbox_1 = self.driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
        checkbox_2 = self.driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")
        assert not checkbox_1.is_selected()
        assert checkbox_2.is_selected()
        checkbox_1.click()
        checkbox_2.click()
        assert checkbox_1.is_selected()
        assert not checkbox_2.is_selected()
        checkbox_1.click()
        checkbox_2.click()
        assert not checkbox_1.is_selected()
        assert checkbox_2.is_selected()

    def test_drag_and_drop(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/drag_and_drop']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Drag and Drop'
        element_a = (WebDriverWait(self.driver, 20)
                     .until(EC.element_to_be_clickable((By.XPATH, "//div[@id='column-a']"))))
        element_b = (WebDriverWait(self.driver, 20)
                     .until(EC.element_to_be_clickable((By.XPATH, "//div[@id='column-b']"))))
        action = ActionChains(self.driver)
        action.drag_and_drop(element_a, element_b).perform()

    def test_base_auth(self):
        self.driver.get('https://admin:admin@the-internet.herokuapp.com')
        self.driver.find_element(By.XPATH, "//a[@href='/basic_auth']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Basic Auth'

    def test_add_remove_elements(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/add_remove_elements/']").click()
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h3").text == 'Add/Remove Elements'
        add_element = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        assert add_element.is_displayed()
        add_element.click()
        delete_elements = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        assert delete_elements.__len__() == 1
        add_element.click()
        add_element.click()
        add_element.click()
        delete_elements = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        assert delete_elements.__len__() == 4
        for i, del_el in enumerate(delete_elements):
            if i % 2 != 0:
                del_el.click()
        delete_elements = self.driver.find_elements(By.XPATH, "//button[text()='Delete']")
        assert delete_elements.__len__() == 2

    def test_dropdown(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/dropdown']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Dropdown List'
        dropdown = self.driver.find_element(By.XPATH, '//select[@id="dropdown"]')
        select = Select(dropdown)
        select.select_by_visible_text('Option 1')
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").is_selected()
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").get_attribute('value') == '1'
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").text == 'Option 1'
        select.select_by_index(2)
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").is_selected()
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").get_attribute('value') == '2'
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").text == 'Option 2'
        select.select_by_value('1')
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").is_selected()
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").get_attribute('value') == '1'
        assert dropdown.find_element(By.XPATH, "//option[@selected='selected']").text == 'Option 1'

    def test_inputs(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/inputs']").click()
        assert self.driver.find_element(By.XPATH, "//div[@id='content']//h3").text == 'Inputs'
        input_element = self.driver.find_element(By.XPATH, '//input')
        assert input_element.get_attribute('value') == ''
        input_element.send_keys('45')
        assert input_element.get_attribute('value') == '45'
        self.driver.refresh()
        input_element = self.driver.find_element(By.XPATH, '//input')
        input_element.send_keys(Keys.ARROW_UP)
        assert input_element.get_attribute('value') == '1'

    def test_iframe(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/frames']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Frames'
        self.driver.find_element(By.XPATH, "//a[@href='/iframe']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == ('An iFrame containing the '
                                                                                         'TinyMCE WYSIWYG Editor')
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        element = self.driver.find_element(By.XPATH, '/html/body/p')
        assert element.text == 'Your content goes here.'
        self.driver.switch_to.default_content()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == ('An iFrame containing the '
                                                                                         'TinyMCE WYSIWYG Editor')

    def test_key_presses(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/key_presses']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Key Presses'
        inp_field = self.driver.find_element(By.XPATH, "//input[@id='target']")
        inp_field.send_keys(Keys.MULTIPLY)
        assert inp_field.get_attribute('value') == '*'

    def test_redirection(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/redirector']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Redirection'
        self.driver.find_element(By.XPATH, "//a[@id='redirect']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Status Codes'
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/200']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/301']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/404']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/500']").is_displayed()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'here')]").click()
        assert self.driver.find_element(By.XPATH,
                                        "//h1[contains(text(),'Hypertext Transfer Protocol (HTTP) Status Code Reg')]").is_displayed()

    def test_status_codes(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/status_codes']").click()
        st_code_200 = self.driver.find_element(By.XPATH, "//a[@href='status_codes/200']")
        st_code_301 = self.driver.find_element(By.XPATH, "//a[@href='status_codes/301']")
        st_code_404 = self.driver.find_element(By.XPATH, "//a[@href='status_codes/404']")
        st_code_500 = self.driver.find_element(By.XPATH, "//a[@href='status_codes/500']")
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Status Codes'
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/200']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/301']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/404']").is_displayed()
        assert self.driver.find_element(By.XPATH, "//a[@href='status_codes/500']").is_displayed()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'here')]").click()
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(),'Hypertext Transfer Protocol (HTTP) Status "
                                                  "Code Reg')]").is_displayed()
        self.driver.back()
        st_code_200.click()
        assert self.driver.current_url == 'https://the-internet.herokuapp.com/status_codes/200'
        self.driver.back()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'here')]").click()
        assert self.driver.find_element(By.XPATH,
                                        "//h1[contains(text(),'Hypertext Transfer Protocol "
                                        "(HTTP) Status Code Reg')]").is_displayed()
        self.driver.back()
        st_code_301.click()
        assert self.driver.current_url == 'https://the-internet.herokuapp.com/status_codes/301'
        self.driver.back()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'here')]").click()
        assert self.driver.find_element(By.XPATH,
                                        "//h1[contains(text(),'Hypertext Transfer Protocol "
                                        "(HTTP) Status Code Reg')]").is_displayed()
        self.driver.back()
        st_code_404.click()
        assert self.driver.current_url == 'https://the-internet.herokuapp.com/status_codes/404'
        self.driver.back()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'here')]").click()
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(),'Hypertext Transfer Protocol "
                                                  "(HTTP) Status Code Reg')]").is_displayed()
        self.driver.back()
        st_code_500.click()
        assert self.driver.current_url == 'https://the-internet.herokuapp.com/status_codes/500'
        self.driver.back()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'here')]").click()
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(),'Hypertext Transfer Protocol "
                                                  "(HTTP) Status Code Reg')]").is_displayed()
        self.driver.back()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Status Codes'
