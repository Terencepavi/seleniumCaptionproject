import time

from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        self.__SignIn_locator = (By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]")
        self.__email_input_locator = (By.ID, "email")
        self.__password_input_locator = (By.ID, "pass")
        self.__Welcometext_locator = (By.XPATH, "//div[@class='panel header']//span[@class='logged-in'][normalize-space()='Welcome, Jacksparrow Captain!']")
        self.__login_locator= (By.XPATH,"(//span[contains(text(),'Sign In')])[1]")
        self.__password_error_text_locator= (By.XPATH,"//div[@id='pass-error']")
        self.__username_error_text_locator = (By.XPATH,"//div[@id='email-error']")

    def enter_username(self, username):
        self.type_by_locator(self.__email_input_locator, username)

    def enter_password(self, password):
        self.type_by_locator(self.__password_input_locator, password)

    def click_on_signin(self):
        self.click_by_locator(self.__SignIn_locator)

    def click_on_login(self):
        self.click_by_locator(self.__login_locator)
    @property
    def get_welcome_message(self):
        return self.get_text_by_locator(self.__Welcometext_locator)

    @property
    def get_username_invalid_error_message(self):
        return self.get_text_by_locator(self.__username_error_text_locator)

    @property
    def get_password_invalid_error_message(self):
        return self.get_text_by_locator(self.__password_error_text_locator)
    #
    # @property
    # def get_username_placeholder(self):
    #     return self.get_attribute_value(self.__username_locator, "placeholder")
    #
    # @property
    # def get_password_placeholder(self):
    #     return self.get_attribute_value(self.__password_locator, "placeholder")
