import time
import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from pages.login_page import LoginPage
from pages.search_product import SearchProduct
from pages.Customer_register_page import RegisterPage
from utilities import data_source

"""Login related test cases """


class TestCreateAccount(WebDriverWrapper):
    @pytest.mark.parametrize("firstname","lastname","password","errormessage",data_source.Create_account)
    def test_search_and_verify_with_displayed_products(self,firstname,lastname,password,errormessage):
        create_page= RegisterPage(self.driver)
        create_page.click_on_homepage_create_account_button()
        create_page.enter_firstname(firstname)
        create_page.enter_lastname(lastname)
        create_page.enter_password(password)
        create_page.click_on_create_button()
        actualerror=create_page.get_password_invalid_error_messages()
        if actualerror==errormessage:
            assert True

