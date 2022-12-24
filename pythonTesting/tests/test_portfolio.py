import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import helpers


@pytest.mark.positive
class Portfolio:
    def test_sectionString(self):
        driver: WebDriver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.get("https://selectors.webdriveruniversity.com/#")
        helpers.waitSeconds(3)

