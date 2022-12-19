import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

def waitSeconds(howLong):
    time.sleep(howLong)

driver.get("https://www.selenium.dev/documentation/webdriver/getting_started/first_script/")
waitSeconds(3)

"""

"""