import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import helpers

#
# class Portfolio:
@pytest.mark.positive
def test_portfolioText():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    portfolioHeaderSelector = "//section[@id='portfolio']//h2[.='Portfolio']"
    portfolioHeaderElement = driver.find_element(By.XPATH, portfolioHeaderSelector)
    assert portfolioHeaderElement.is_displayed()

@pytest.mark.positive
def test_starIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    starSelector = "#portfolio .divider-custom"
    starElement = driver.find_element(By.CSS_SELECTOR, starSelector)
    assert starElement.is_displayed()


