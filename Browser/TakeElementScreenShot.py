from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.example.com")
ele = driver.find_element(By.CSS_SELECTOR, "p")

ele.screenshot("./image.png")