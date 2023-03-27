import time
import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from pages.login_page import LoginPage
from pages.search_product import SearchProduct
from utilities import data_source

"""Login related test cases """


class TestSearch_Product(WebDriverWrapper):
    @pytest.mark.parametrize("productname", data_source.product_names)
    def test_search_and_verify_with_displayed_products(self,productname):
        search_page= SearchProduct(self.driver)
        search_page.enter_product_name(productname)
        search_page.click_search_icon()
        time.sleep(5)
        products=self.driver.find_elements(By.CSS_SELECTOR,'strong[class="product name product-item-name"]')
        total=len(products)
        print(total)
        assert_that("12").is_equal_to(total)
    # def test_empty_error_message(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.click_on_signin()
    #     login_page.click_on_login()
    #     assert_that("This is a required field.").is_equal_to(login_page.get_username_invalid_error_message)
    #     assert_that("This is a required field.").is_equal_to(login_page.get_password_invalid_error_message)
