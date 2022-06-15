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

    def test_check_categories_detail(self):
        #check image in categories
        driver.find_elements_by_css_selector("H8mXLe")
        #check name in categories
        driver.find_elements_by_css_selector("C9kwfl")  

    def test_check_categories(self):
        driver.find_elements_by_css_selector("_1l+Pw-")
    



    


if __name__ == "__main__":
    unittest.main()