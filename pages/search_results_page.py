from pages.base_page import BasePage

class MainPage(BasePage):
    BUTTON_NOT_NOW = (By.XPATH, "//button[text() = 'Not Now']")
    FIELD_SEARCH = (By.XPATH, "//input[@placeholder = 'Search']")

    def type_in_search_field(self, param):
        self.type_in(self.FIELD_SEARCH, "#fitness")

    def click_result_with_text(self, text):
        RESULT = (By.XPATH, "")