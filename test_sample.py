import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    # Configure Chrome options for headless automation
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Automatically install and initialize ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_google_title(driver):
    """Verify that navigating to Google loads the expected page title."""
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_search_interaction(driver):
    """Verify searching for a term produces updated page contents."""
    driver.get("https://www.google.com")

    # Locate the search input box by its 'q' name attribute
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys("Selenium Testing with Jenkins")
    search_box.submit()

    # Assert the title changes to include the search term
    WebDriverWait(driver, 10).until(
        EC.title_contains("Selenium Testing with Jenkins")
    )
    assert "Selenium Testing with Jenkins" in driver.title