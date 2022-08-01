from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(By.ID, "file-upload").send_keys("/home/user17/Desktop/Selenium/Upload/images.jpeg")
driver.find_element(By.ID, "file-submit").click()
if(driver.page_source.find("File Uploaded!")):
    print("File upload success")
else:
    print("File upload failed") 
