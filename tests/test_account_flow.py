import sys
import os
import time
from selenium.common.exceptions import TimeoutException

# Add root path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage

# Test Data
test_email = f"nikita.bawage{int(time.time())}@testmail.com"
test_first_name = "Nikita"
test_last_name = "Bawage"
test_password = "Test@1234"

# Screenshot helper
def take_screenshot(driver, name):
    timestamp = int(time.time())
    filename = f"screenshots/{name}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")

def test_account_creation_and_login():
    driver = get_driver()
    driver.get("https://magento.softwaretestingboard.com/")
    take_screenshot(driver, "home_page_loaded")
    print(f"Creating account for: {test_email}")

    # Create account
    home_page = HomePage(driver)
    home_page.go_to_create_account()
    take_screenshot(driver, "create_account_page")

    create_account_page = CreateAccountPage(driver)
    create_account_page.enter_first_name(test_first_name)
    create_account_page.enter_last_name(test_last_name)
    create_account_page.enter_email(test_email)
    create_account_page.enter_password(test_password)
    create_account_page.enter_confirm_password(test_password)
    create_account_page.click_create_account()
    take_screenshot(driver, "account_created")

    # Logout
    home_page.logout()
    take_screenshot(driver, "logged_out")

    # 🔁 Open login page in new tab
    driver.execute_script("window.open('https://magento.softwaretestingboard.com/customer/account/login/', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    take_screenshot(driver, "login_page_new_tab")

    # Login
    login_page = LoginPage(driver)
    login_page.enter_email(test_email)
    login_page.enter_password(test_password)
    login_page.click_login()
    take_screenshot(driver, "logged_in")

    # Switch back to original tab if needed
    driver.switch_to.window(driver.window_handles[0])

    # Verify login
    home_page = HomePage(driver)
    assert home_page.is_user_logged_in(), "❌ Login verification failed"
    take_screenshot(driver, "login_verified")
    print("Login verified")

    driver.quit()

if __name__ == "__main__":
    test_account_creation_and_login()
