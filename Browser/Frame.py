from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/webdriver/browser/frames/")

# move to frame

driver.switch_to.frame("buttonframe")

driver.find_element(By.TAG_NAME, "button").click()

# move back default content
driver.switch_to.default_content()