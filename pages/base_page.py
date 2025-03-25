from typing import Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from config.environment import Environment

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.env = Environment()
        self.wait = WebDriverWait(driver, self.env.explicit_wait)

    def find_element(self, locator: tuple) -> WebElement:
        """Find element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """Find elements with explicit wait"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: tuple) -> None:
        """Click element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator: tuple, text: str) -> None:
        """Send keys to element with explicit wait"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get text from element with explicit wait"""
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator: tuple) -> bool:
        """Check if element is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_element_present(self, locator: tuple) -> bool:
        """Check if element is present in DOM"""
        try:
            self.find_element(locator)
            return True
        except:
            return False 