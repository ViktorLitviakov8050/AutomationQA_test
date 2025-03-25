import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import BASE_URL, IMPLICIT_WAIT

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(IMPLICIT_WAIT)
    yield driver
    driver.quit()

def test_example(driver):
    driver.get(BASE_URL)
    assert driver.title is not None 