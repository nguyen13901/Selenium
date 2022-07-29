from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")

original_window = driver.current_window_handle

# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
driver.switch_to.new_window('window')

print("Width 1: ", driver.get_window_size().get("width"))
print("Height 1: ", driver.get_window_size().get("height"))

driver.close()

driver.switch_to.window(original_window)
# driver.maximize_window()
driver.minimize_window()

print("Width 2: ", driver.get_window_size().get("width"))
print("Height 2: ", driver.get_window_size().get("height"))
