from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")
driver.save_screenshot("./image.png")