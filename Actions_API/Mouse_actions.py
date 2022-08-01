from argparse import Action
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


driver = webdriver.Chrome()

driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

clickable = driver.find_element(By.ID, "clickable")

# Click and hold
# ActionChains(driver)\
#     .click_and_hold(clickable)\
#     .perform()

# Click and release
# ActionChains(driver)\
#     .click(clickable)\
#     .pefomrm()

# Context click

# ActionChains(driver)\
#     .context_click(clickable)\
#     .perform()

# Back Click

# driver.get("https://google.com")

# action = ActionBuilder(driver)
# action.pointer_action.pointer_down(MouseButton.BACK)
# action.pointer_action.pointer_up(MouseButton.BACK)
# action.perform()

# driver.back()

# Forward Click

# action = ActionBuilder(driver)
# action.pointer_action.pointer_down(MouseButton.FORWARD)
# action.pointer_action.pointer_up(MouseButton.FORWARD)
# action.perform()

# Double click

# clickable = driver.find_element(By.ID, "clickable")
# ActionChains(driver)\
#     .double_click(clickable)\
#     .perform()

# Move to element

# hoverable = driver.find_element(By.ID, "hover")
# ActionChains(driver)\
#     .move_to_element(hoverable)\
#     .perform()

# Move by offset 
# Offset from Element

# mouse_tracker = driver.find_element(By.ID, "mouse-tracker")
# ActionChains(driver)\
#     .move_to_element_with_offset(mouse_tracker, 8, 11)\
#     .perform()

# Offset from Viewport 
action = ActionBuilder(driver)
action.pointer_action.move_to_location(8, 12)
action.perform()

# Offset from Current Pointer Location

# ActionChains(driver)\
#     .move_by_offset( 13, 15)\
#     .perform()

# Drag and drop on element
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")
ActionChains(driver)\
    .drag_and_drop(draggable, droppable)\
    .perform()