from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.example.com")

# Tag name

# attr = driver.find_element(By.CSS_SELECTOR, "h1").tag_name

# print(attr)

# Is Selected 

# driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Returns true if element is checked else returns false
# value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()

# print(value)

    # Navigate to url
# driver.get("http://www.google.com")

    # Returns true if element is enabled else returns false
# value = driver.find_element(By.NAME, 'btnK').is_enabled()

# print(value)

    # Navigate to url
driver.get("https://www.example.com")

    # Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.CSS_SELECTOR, "h1").rect

cssValue = driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('color')

text = driver.find_element(By.CSS_SELECTOR, "p").text

print(res)

print(cssValue)

print(text)