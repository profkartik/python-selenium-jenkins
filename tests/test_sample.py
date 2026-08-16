import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    options = Options()
    # Headless mode is essential for CI/Jenkins execution without a monitor
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Automatically downloads and configures the matching ChromeDriver binary
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_search_interaction(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Jenkins Automation Testing")
    search_box.submit()
    assert len(driver.title) > 0