from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://google.com")
driver.implicitly_wait(10)
driver.get("https://facebook.com")
driver.back()
driver.forward()
driver.refresh()

driver.quit()