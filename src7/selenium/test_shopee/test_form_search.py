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


    def test_check_form_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-searchbar-input")
    
    def test_check_button_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-svg-icon")

    def test_check_input_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input")

if __name__ == "__main__":
    unittest.main()