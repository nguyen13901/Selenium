from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")

driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

wait = WebDriverWait(driver, 10)

# Three methods to storage alert
# Method 1
# alert = wait.until(expecteds_conditions.alert_is_present())

# Method 2 
# wait.until(expecteds_conditions.alert_is_present)
# alert = driver.swith_to.alert

# Method 3
wait.until(expected_conditions.alert_is_present())
alert = Alert(driver)

print("Text: ", alert.text)

# Type your message
alert.send_keys("I love u")

# Press the OK button
alert.accept()
