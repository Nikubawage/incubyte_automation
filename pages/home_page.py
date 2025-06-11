# home_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import time

class HomePage(BasePage):
    CREATE_ACCOUNT_LINK = (By.XPATH, "//div[@class='panel header']//a[text()='Create an Account']")
    LOGIN_LINK = (By.XPATH, "//div[@class='panel header']//a[text()='Sign In']")
    DROPDOWN_BUTTON = (By.XPATH, "//div[@class='panel header']//button")
    SIGN_OUT_LINK = (By.LINK_TEXT, "Sign Out")
    USER_GREETING = (By.XPATH, "//div[@class='panel header']//span[contains(text(),'Welcome')]")

    def go_to_create_account(self):
        self.wait_for_page_load()
        self.wait_for_element_clickable(self.CREATE_ACCOUNT_LINK).click()
        print("✅ Navigated to Create Account page")

    def go_to_login(self):
        self.wait_for_page_load()
        retries = 2
        for attempt in range(retries):
            try:
                login_link = self.wait_for_element_clickable(self.LOGIN_LINK)
                login_link.click()
                print("✅ Clicked Sign In link")
                return
            except TimeoutException:
                print(f"⚠️ Attempt {attempt + 1} failed: Sign In link not clickable")
                time.sleep(2)
        raise TimeoutException("❌ Unable to click Sign In link after multiple retries")

    def logout(self):
        dropdown = self.wait_for_element_clickable(self.DROPDOWN_BUTTON)
        dropdown.click()

        sign_out = self.wait_for_element_clickable(self.SIGN_OUT_LINK)
        sign_out.click()

        self.wait_for_url_contains("logout")
        print("✅ Successfully Logged Out")
        time.sleep(2)

    def is_user_logged_in(self):
        try:
            return self.is_element_visible(self.USER_GREETING)
        except:
            return False
