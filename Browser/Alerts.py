from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")

# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

# wait
wait = WebDriverWait(driver, 10)

# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()