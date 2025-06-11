from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    CUSTOMER_NAME = (By.CLASS_NAME, "customer-name")
    DROPDOWN = (By.XPATH, "//div[@class='panel header']//button")
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")

    def logout(self):
        self.click(self.DROPDOWN)
        self.click(self.SIGN_OUT)