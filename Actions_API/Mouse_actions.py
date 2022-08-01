from argparse import Action
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

clickable = driver.find_element(By.ID, "clickable")

# Click and hold
ActionChains(driver)\
    .click_and_hold(clickable)\
    .perform()

# Click and release
ActionChains(driver)\
    .click(clickable)\
    .pefomrm()

