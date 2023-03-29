import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class SearchProduct(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        self.__search_box_locator = (By.XPATH, "//input[@id='search']")
        self.__total_product_count_locator = (By.XPATH,"//div[@class='column main']//div[1]//p[1]//span[2]")
        self.__product_displayed_page = (By.CSS_SELECTOR, 'strong[class="product name product-item-name"]')
        self.__search_icon_locator = (By.XPATH, "(//button[@title='Search'])[1]")

    def enter_product_name(self, productname):
        self.type_by_locator(self.__search_box_locator,productname)

    def total_product_dispalyed(self):
        self.driver.find_elements(By.CSS_SELECTOR, 'strong[class="product name product-item-name"]')

    def total_product_count(self):
        return self.get_text_by_locator(self.__total_product_count_locator)

    def click_search_icon(self):
        self.click_by_locator(self.__search_icon_locator)


