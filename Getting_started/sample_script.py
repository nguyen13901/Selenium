from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.common.by import By

def sample_script():
    driver = webdriver.Chrome()

    driver.get("https://google.com")

    driver.implicitly_wait(10)

    get_information_browser(driver)

    get_information_elements(driver)


    # driver.quit()

def get_information_browser(driver):
    title = driver.title
    print("Title of browser: ", title)

def get_information_elements(driver):
    # find elements
    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    # take_action
    search_box.send_keys("Selenium")
    search_button.click()

    # Get information on element
    # search_box = driver.find_element(by=By.NAME, value="q")
    # value = search_box.get_attribute("title")

    # print("Value: ", value)
    print(type(search_box))
    



sample_script()