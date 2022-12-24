import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import helpers


@pytest.mark.positive
def test_monitorImageIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    imageSelector = "[alt='code-icon']"
    playgroundHeaderElement = driver.find_element(By.CSS_SELECTOR, imageSelector)
    assert playgroundHeaderElement.is_displayed()

@pytest.mark.positive
def test_selectorPlaygroundTextIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    textSelector = "/html//body[@id='page-top']//h1[.='Selector Playground']"
    playgroundTextElement = driver.find_element(By.XPATH, textSelector)
    assert playgroundTextElement.is_displayed()

@pytest.mark.positive
def test_starIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    starSelector = ".align-items-center .divider-custom"
    starElement = driver.find_element(By.CSS_SELECTOR, starSelector)
    assert starElement.is_displayed()

@pytest.mark.positive
def test_seleniumCypressWebdriverTextIsDisplayed():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    technologiesSelector = "/html//body[@id='page-top']//p[.='Selenium WebDriver - Cypress - WebdriverIO']"
    technologiesElement = driver.find_element(By.XPATH, technologiesSelector)
    assert technologiesElement.is_displayed()\
