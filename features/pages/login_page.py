from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage

class LoginPage(BasePage):
    FIELD_USERNAME = (By.NAME, "username")
    FIELD_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")

# test
    def enter_username(self, username):
        self.type_in(self.FIELD_USERNAME, username)

    def enter_password(self, password):
        self.type_in(self)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send.keys(password)

    def login(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()




