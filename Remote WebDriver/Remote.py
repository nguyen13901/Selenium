from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

chrome_options = Options()

chrome_options.set_capability("browserVersion", "103")
chrome_options.set_capability("platformName", "Ubuntu")
driver = webdriver.Remote(
    command_executor='http://www.example.com',
    options = chrome_options
)

driver.get("http://www.google.com")

