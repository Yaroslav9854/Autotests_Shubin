import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome ()

driver.get("https://www.litres.ru")
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.fixture(scope='function')
def close_session():
    yield
    driver.quit()

def test_dz_8(close_session):
    search = driver.find_element(By.CSS_SELECTOR, "input._8fba8811")
    search.click()
    search.send_keys("Пушкин")

    search_button = driver.find_element(By.CSS_SELECTOR, "button._82b1c248")
    search_button.click()

    # WebDriverWait(driver, 10).until(
    #     expected_conditions.visibility_of_element_located((By.XPATH, '//a[@data-testid="art__title"]'))
    # )
    #
    # books = driver.find_elements(By.XPATH, "//a[@data-testid="art__title"]")
    #
    # print(f"\nНайдено книг на странице: {len(books)}")
    # print("Название первых 5 книг:")
    #
    # for i, title in enumerate(books[:5], start=1):
    #     print(f"{i}. {title.text}")