import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestExample(BasePage):
    def test_example(self, driver, base_url):
        """Example test demonstrating framework usage"""
        self.driver = driver
        self.driver.get(base_url)
        
        # Example assertions
        assert self.driver.title is not None
        assert self.is_element_present((By.TAG_NAME, "body")) 