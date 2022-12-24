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
def test_portfolioIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    portfolioSelector = "PORTFOLIO"
    portfolioElement = driver.find_element(By.LINK_TEXT, portfolioSelector)
    assert portfolioElement.is_displayed()

@pytest.mark.positive
def test_playgroundIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    playgroundSelector = "PLAYGROUND"
    playgroundElement = driver.find_element(By.LINK_TEXT, playgroundSelector)
    assert playgroundElement.is_displayed()
@pytest.mark.positive
def test_contactIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    contactSelector = "CONTACT"
    contactElement = driver.find_element(By.LINK_TEXT, contactSelector)
    assert contactElement.is_displayed()
