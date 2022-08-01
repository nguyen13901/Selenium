from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


driver = webdriver.Chrome()
driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

clickable = driver.find_element(By.ID, "clickable")

# Key down
# ActionChains(driver)\
#     .move_to_element(clickable)\
#     .pause(1)\
#     .click_and_hold()\
#     .pause(1)\
#     .key_down(Keys.SHIFT)\
#     .send_keys("abc")\
#     .perform()

# Key up
# ActionChains(driver)\
#     .move_to_element(clickable)\
#     .pause(1)\
#     .click_and_hold()\
#     .pause(1)\
#     .key_down(Keys.SHIFT)\
#     .send_keys("a")\
#     .key_up(Keys.SHIFT)\
#     .send_keys("b")\
#     .perform()

# Send keys
# Active Element

# ActionChains(driver)\
#     .move_to_element(clickable)\
#     .pause(1)\
#     .click_and_hold()\
#     .pause(1)\
#     .send_keys("abc")\
#     .perform()

# Designated Element

# ActionChains(driver)\
#     .send_keys_to_element(clickable, "abc")\
#     .perform()

# Copy and Paste

# ActionChains(driver)\
#     .send_keys_to_element(clickable, "Selenium!")\
#     .pause(1)\
#     .key_down(Keys.SHIFT)\
#     .pause(1)\
#     .send_keys(Keys.ARROW_UP)\
#     .pause(1)\
#     .key_up(Keys.SHIFT)\
#     .pause(1)\
#     .key_down(Keys.CONTROL)\
#     .pause(1)\
#     .send_keys("c")\
#     .pause(1)\
#     .key_up(Keys.CONTROL)\
#     .pause(1)\
#     .send_keys(Keys.ARROW_RIGHT)\
#     .pause(1)\
#     .key_down(Keys.CONTROL)\
#     .pause(1)\
#     .send_keys("v")\
#     .pause(1)\
#     .key_up(Keys.CONTROL)\
#     .perform()
