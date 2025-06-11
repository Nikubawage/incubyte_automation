from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    # Safe options for running inside Codespaces or headless environments
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Optional: disable GPU usage (saves resources)
    options.add_argument("--disable-gpu")

    # ✅ Use ChromeDriverManager to avoid path issues
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)