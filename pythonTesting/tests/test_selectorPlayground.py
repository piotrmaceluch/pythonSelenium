import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def waitSeconds(howLong):
    time.sleep(howLong)


def test_playgroundHeader():
    driver: WebDriver = webdriver.Chrome(
        service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.get("https://selectors.webdriveruniversity.com/#")
    waitSeconds(3)

    playground = ".page-section-heading"
    playgroundHeader = driver.find_element(By.CSS_SELECTOR, playground)
    assert playgroundHeader.is_displayed()
