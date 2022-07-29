from requests import head
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.example.com")
# Stores the header element
header = driver.find_element(By.CSS_SELECTOR, "h1")

# Executing JavaScript to capture innerText of header element
driver.execute_script('return arguments[0].innerText', header)
