from pages.base.page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL = "https://example.com/auth"
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = ()
    LOGIN_BUTTON = ()
    WELCOME_TEXT = ()

    def __init__(self,   driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_email(self, email):
        self.wait_element(self.EMAIL_INPUT).send_keys(email)
        return self

    def enter_password(self, password):
        return self

    def check_enter_text(self):
        return self.driver.find_elements("id", "welcome_text").text