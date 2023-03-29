import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class RegisterPage(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        self.__Create_account_locator = (By.XPATH, "(//a[normalize-space()='Create an Account'])[1]")
        self.__firstname_input_locator = (By.ID, "firstname")
        self.__lastname_input_locator = (By.ID, "lastname")
        self.__email_input_locator = (By.ID,"email_address")
        self.__password_input_locator= (By.ID,"password")
        self.__password_confirm_input_locator= (By.ID,"password-confirmation")
        self.__create_button_locator = (By.CSS_SELECTOR,"button[title='Create an Account'] span")
        self.__error_msg_password= (By.ID,"password-error")

    def click_on_homepage_create_account_button(self):
        self.click_by_locator(self.__Create_account_locator)
    def enter_firstname(self, firstname):
        self.type_by_locator(self.__firstname_input_locator, firstname)
    def enter_lastname(self,lastname):
        self.type_by_locator(self.__lastname_input_locator,lastname)
    def enter_email(self,email):
        self.type_by_locator(self.__email_input_locator,email)
    def enter_password(self,password):
        self.type_by_locator(self.__password_input_locator,password)

    def enter_confirm_password(self,confirmpassword):
        self.type_by_locator(self.__password_confirm_input_locator,confirmpassword)

    def click_on_create_button(self):
        self.click_by_locator(self.__create_button_locator)

    def get_password_invalid_error_messages(self):
        return self.get_text_by_locator(self.__error_msg_password)

