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

    def test_check_flash_sale(self):
        driver.find_elements_by_css_selector("flash-sale-item-card flash-sale-item-card--home-page flash-sale-item-card--VN")

    def test_check_flash_sale_detail(self):
        # % sale
        driver.find_elements_by_css_selector("_5ICO3M yV54ZD X7gzZ7 shopee-badge")
        # image product sale 
        driver.find_elements_by_css_selector("flash-sale-item-card__image flash-sale-item-card__image--home-page")
        # price product sale
        driver.find_elements_by_css_selector("flash-sale-item-card__lower-wrapper flash-sale-item-card__lower-wrapper--VN flash-sale-item-card__lower-wrapper--home-page")
    



if __name__ == "__main__":
    unittest.main()