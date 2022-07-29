from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_chrome_session():
    # options = Options()
    
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()

    driver.get("https://google.com/")

    driver.quit()

test_chrome_session()   