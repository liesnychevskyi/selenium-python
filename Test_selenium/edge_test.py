
from selenium import webdriver
import time

driver = webdriver.Edge()

driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
time.sleep(2)
driver.refresh()
driver.quit()
