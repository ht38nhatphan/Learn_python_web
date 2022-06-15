from logging import error
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
s = "/html[@class='mdl-js']/body[@class='nt-s nl-l']/div[@id='main']/div/header[@class='shopee-top shopee-top--sticky']/div[@class='container-wrapper header-with-search-wrapper']/div[@class='container header-with-search']/div[@class='header-with-search__search-section']/div[@class='shopee-searchbar']/button[@class='btn btn-solid-primary btn--s btn--inline shopee-searchbar__search-button']"
class Shopeeweb(unittest.TestCase):
    def setUp(self):
        driver.get("https://shopee.vn/")

    def test_check_product(self):
        # driver.find_element(By.CLASS_NAME,"W3bJfG")
        driver.find_elements_by_css_selector("yZLQT4 YbTQos")

    def test_check_product_detail(self):
        #check image
        driver.find_elements_by_css_selector("n-CE6j iR+sxV")
        #check name
        # self.assertEqual(driver.find_element(By.CLASS_NAME,"vc0PvV AxYdVM").text,"[HCM]Dép Quai Ngang Nam Nữ EVA Cao Cấp Siêu Nhẹ Đế Cao 4cm Chống Nước") 
        driver.find_elements_by_css_selector("vc0PvV AxYdVM")
        #check price
        # self.assertEqual(driver.find_element(By.CLASS_NAME,"j0vBz2").text,"59.000")
        driver.find_elements_by_css_selector("j0vBz2")
    
    


if __name__ == "__main__":
    unittest.main()