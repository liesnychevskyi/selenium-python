
from selenium import webdriver
import time

# driver = webdriver.Firefox("C:\\Users\\liesn\\PycharmProjects\\SeleniumLearning\\drivers\\geckodriver.exe")
driver = webdriver.Firefox()
# driver.set_page_load_timeout(2)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
time.sleap(4)
driver.quit()
