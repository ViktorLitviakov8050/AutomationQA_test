from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.environment import Environment

class DriverFactory:
    @staticmethod
    def get_driver(browser_name: Optional[str] = None) -> webdriver.Remote:
        """
        Create and return a WebDriver instance based on browser name
        """
        env = Environment()
        browser = browser_name or env.browser_name

        if browser.lower() == 'chrome':
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            if env.is_headless:
                options.add_argument('--headless')
            return webdriver.Chrome(service=service, options=options)
        
        elif browser.lower() == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            if env.is_headless:
                options.add_argument('--headless')
            return webdriver.Firefox(service=service, options=options)
        
        else:
            raise ValueError(f"Browser {browser} is not supported") 