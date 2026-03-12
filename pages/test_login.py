class LoginPage:
    URL = "https://example.com/auth"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_email(self):
        self.driver.find_elements("id", "email").send_keys("email@mail.ru")
        return self

    def enter_password(self):
        return self

    def click_login(self):
        return self

    def check_enter_text(self):
        return self