from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome("..\\drivers\\chromedriver.exe")
driver = webdriver.Chrome()

driver.maximize_window()
# driver.set_page_load_timeout(2)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
# driver.find_element_by_name("btnK").click()
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  # it is like click
time.sleep(1)
driver.quit()
