import os
import pytest
from typing import Generator
from selenium.webdriver.remote.webdriver import WebDriver
from utils.driver_factory import DriverFactory
from config.environment import Environment

@pytest.fixture(scope="session")
def env() -> Environment:
    """Environment configuration fixture"""
    return Environment()

@pytest.fixture(scope="function")
def driver(env: Environment) -> Generator[WebDriver, None, None]:
    """WebDriver fixture"""
    driver = DriverFactory.get_driver()
    driver.implicitly_wait(env.implicit_wait)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def base_url(env: Environment) -> str:
    """Base URL fixture"""
    return env.base_url 