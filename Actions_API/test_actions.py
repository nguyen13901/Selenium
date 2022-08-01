from signal import pause
from time import time


from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By


def test_pause(driver):
    driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

    start = time()

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .move_to_element(clickable)\
        .pause(1)\
        .click_and_hold()\
        .pause(1)\
        .send_keys("abc")\
        .perform()

    duration = time() - start
    assert duration > 2
    assert duration < 3
    print("Duration:", duration)


def test_release_all(driver):
    driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")

    clickable = driver.find_element(By.ID, "clickable")
    
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .key_down(Keys.SHIFT)\
        .key_down(Keys.ALT)\
        .key_down("a")\
        .perform()

    ActionBuilder(driver).clear_actions()                                                           

    ActionChains(driver)\
    .key_down('a')\
    .key_down('b')\
    .perform()

    assert clickable.get_attribute('value')[0] == "Â"
    assert clickable.get_attribute('value')[1] == "a"

    print("values: ", clickable.get_attribute('value'))


driver = webdriver.Chrome()

test_pause(driver)
test_release_all(driver)

