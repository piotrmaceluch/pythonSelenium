import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def waitSeconds(howLong):
    time.sleep(howLong)

if __name__ == '__main__':
    print_hi('PyCharm')

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/webdriver/getting_started/first_script/")
waitSeconds(3)