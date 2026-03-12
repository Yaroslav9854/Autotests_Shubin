import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.quit()