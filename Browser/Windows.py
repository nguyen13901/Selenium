from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumhq.github.io")

wait = WebDriverWait(driver, 10)

original_window = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Register now!").click()

# Wait for the new window or tab
# wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

wait.until(EC.title_is("Selenium Conf 2022 - Online | ConfEngine - Conference Platform"))

driver.back()
# driver.forward()


