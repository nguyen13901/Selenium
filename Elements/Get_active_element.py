from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://google.com")

driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

attr = driver.switch_to.active_element.get_attribute("title")
print(attr) 