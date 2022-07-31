from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.file_detector import LocalFileDetector

driver = webdriver.Chrome()

driver.file_detector = LocalFileDetector()

driver.get("http://sso.dev.saucelabs.com/test/guinea-file-upload")

driver.find_element(By.ID, "myfile").send_keys("/Users/sso/the/local/path/to/darkbulb.jpg")