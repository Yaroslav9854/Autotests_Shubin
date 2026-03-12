import pytest
import selenium
from selenium import webdriver

driver = webdriver.Chrome ()

driver.get("https://toolsqa.com")
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.fixture(scope='function')
def close_session():
    yield
    driver.quit()

def test_dz_sel(close_session):
    search = driver.find_element(By.CSS_SELECTOR, "")
    search.click()
    search.send_keys("Demo Site")

    search_button = driver.find_element(By.CSS_SELECTOR, "")
    search_button.click()