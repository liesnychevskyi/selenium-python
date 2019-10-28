from selenium import webdriver
import time
import unittest
import sys  # for running in CLI
import os  # for running in CLI

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from pom_demo.pages.loginPage import LoginPage
from pom_demo.pages.homePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path="/Users/Stan/Desktop/selenium_drivers/drivers/chromedriver")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver  # shortcut

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test passed...")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/Stan/PycharmProjects/selenium-python/pom_demo/html_report'))

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(executable_path="/Users/Stan/Desktop/selenium_drivers/drivers/chromedriver")
    #     cls.driver.implicitly_wait(10)
    #     cls.driver.maximize_window()
    #
    # def test_login_valid(self):
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.driver.find_element_by_id("txtUsername").send_keys("Admin")
    #     self.driver.find_element_by_id("txtPassword").send_keys("admin123")
    #     self.driver.find_element_by_id("btnLogin").click()
    #     self.driver.find_element_by_id("welcome").click()
    #     self.driver.find_element_by_link_text("Logout").click()
    #
    # @classmethod
    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()
    #     print("Test passed...")
