from selenium import webdriver


from selenium.webdriver.chrome.options import Options
options = Options()

# options.page_load_strategy = 'normal'
# options.page_load_strategy = 'eager'
# options.page_load_strategy = 'none'

driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
driver.quit()