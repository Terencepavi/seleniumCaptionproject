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
        print(search_page.total_product_count())
        products=self.driver.find_elements(By.CSS_SELECTOR,'strong[class="product name product-item-name"]')
        total=len(products)
        print(total)
        if total==search_page.total_product_count():
            assert True
        else:
            assert False