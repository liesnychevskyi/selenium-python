from pom_demo.locators.locators import Locators


class LoginPage():

    def __init__(self, driver):  # constructor for elements initializing
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        # self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
