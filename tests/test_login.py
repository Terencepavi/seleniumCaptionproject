import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listener import WebDriverWrapper
from pages.login_page import LoginPage
from utilities import data_source

"""Login related test cases """


class TestLogin(WebDriverWrapper):
    def test_title(self):
     actual_title = self.driver.title
     assert_that("Home Page").is_equal_to(actual_title)

    @pytest.mark.parametrize("username, password, expected_welcome_msg", data_source.test_valid_login_data)
    def test_valid_login(self,username, password, expected_welcome_msg):
        login_page = LoginPage(self.driver)
        login_page.click_on_signin()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_login()
        assert_that(expected_welcome_msg).is_equal_to(login_page.get_welcome_message)

    """Invalid Login Test - Data Driven Using .csv file"""
    @pytest.mark.parametrize("username, password, expected_error_msg", data_source.login_data_invalid)
    def test_invalid_login(self,username, password,expected_error_msg):
        login_page = LoginPage(self.driver)
        login_page.click_on_signin()
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_on_login()
        assert_that(expected_error_msg).is_equal_to(login_page.get_username_invalid_error_message)

    def test_empty_error_message(self):
        login_page = LoginPage(self.driver)
        login_page.click_on_signin()
        login_page.click_on_login()
        assert_that("This is a required field.").is_equal_to(login_page.get_username_invalid_error_message)
        assert_that("This is a required field.").is_equal_to(login_page.get_password_invalid_error_message)