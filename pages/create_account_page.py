from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CreateAccountPage(BasePage):

    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.ID, "email_address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "password-confirmation")
    CREATE_BUTTON = (By.XPATH, "//button[@title='Create an Account']")

    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME_INPUT, last_name)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def enter_confirm_password(self, confirm_password):
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, confirm_password)

    def click_create_account(self):
        self.click(self.CREATE_BUTTON)
