from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


driver = webdriver.Chrome()
driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

#Scroll to element

# iframe = driver.find_element(By.TAG_NAME, "iframe")
# ActionChains(driver)\
#     .scroll_to_element(iframe)\
#     .perform()

#Scroll by given amount

# footer = driver.find_element(By.TAG_NAME, "footer")
# delta_y = footer.rect["y"]

# ActionChains(driver)\
#     .scroll_by_amount(0, delta_y)\
#     .perform()

# Scroll from an element by a given amount

iframe = driver.find_element(By.TAG_NAME, "iframe")
scroll_origin = ScrollOrigin.from_element(iframe)
ActionChains(driver)\
    .scroll_from_origin(scroll_origin, 0, 200)\
    .perform()