from selenium import webdriver
from selenium.webdriver.chrome.service import Service

browser_path = 'D:/chrome-win64/chrome-win64/chrome.exe'
driver_path = 'D:/chromedriver-win64/chromedriver-win64/chromedriver.exe'

def setup():
    op = webdriver.ChromeOptions()
    op.binary_location = browser_path
    op.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=op, service=Service(executable_path=driver_path))
    driver.maximize_window()
    return driver

def teardown(driver):
    driver.close()