from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

service = Service(executable_path="chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service)

options = Options()
driver = webdriver.Chrome(options=options)

driver.quit()