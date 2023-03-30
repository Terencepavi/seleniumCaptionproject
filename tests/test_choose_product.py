import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestChooseProduct(WebDriverWrapper):
    def test_choose(self):
        @pytest.mark.parametrize("jacket,Size", data_source.Product_choose)
        def test_product(self, jacket, Size):
            self.test_valid_login()
            action = webdriver.ActionChains(self.driver)
            action.move_to_element(self.driver.find_element(By.XPATH, "//span[normalize-space()='Women']")).perform()
            action.move_to_element(self.driver.find_element(By.XPATH,'(//span[normalize-space()="Tops"])[2]')).perform()
            self.driver.find_element(By.XPATH, '(//span[normalize-space()="Jackets"])[2]').click()
            Jacket1 = self.driver.find_element(By.XPATH, "//a[@class='product-item-link'][normalize-space()='" + str(
                jacket) + "']").click()
            self.driver.find_element(By.XPATH, "//div[@option-label='" + str(Size) + "']").click()
            self.driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-50']").click()
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"))
            )
            self.driver.find_element(By.XPATH, "//span[@class='counter-number']").click()
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='top-cart-btn-checkout']"))
            )
            self.driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()