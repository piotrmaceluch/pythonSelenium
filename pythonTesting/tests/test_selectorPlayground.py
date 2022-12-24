import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

import helpers


@pytest.mark.positive
def test_monitorImage():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    playground = "[alt='code-icon']"
    playgroundHeader = driver.find_element(By.CSS_SELECTOR, playground)
    assert playgroundHeader.is_displayed()

@pytest.mark.positive
def test_selectorPlaygroundText():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    text = "/html//body[@id='page-top']//h1[.='Selector Playground']"
    playgroundHeader = driver.find_element(By.XPATH, text)
    assert playgroundHeader.is_displayed()

@pytest.mark.positive
def test_seleniumCypressWebdriverText():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    helpers.waitSeconds(3)

    text = "/html//body[@id='page-top']//p[.='Selenium WebDriver - Cypress - WebdriverIO']"
    playgroundHeader = driver.find_element(By.XPATH, text)
    assert playgroundHeader.is_displayed()
