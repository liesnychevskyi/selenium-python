
from selenium import webdriver
import time

# driver = webdriver.Firefox("C:\\Users\\liesn\\PycharmProjects\\SeleniumLearning\\drivers\\geckodriver.exe")
driver = webdriver.Firefox(executable_path="/Users/Stan/Desktop/selenium_drivers/drivers/geckodriver")
# driver = webdriver.Firefox()
# driver.set_page_load_timeout(2)
driver.get("http://google.com")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleap(4)
driver.find_element_by_xpath("btnK").click()
time.sleap(4)
driver.quit()
