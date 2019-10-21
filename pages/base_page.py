
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.driver.find_element_by_name("password").send_keys(password)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable).click()


