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

    def test_card(self):
        driver.find_element(By.CLASS_NAME,"cart-drawer-container")

    def test_check_button_next(self):
        driver.find_elements_by_css_selector("carousel-arrow carousel-arrow--next carousel-arrow--hint")
   
    def test_check_button_see_all(self):
        driver.find_elements_by_css_selector("shopee-button-no-outline")
   
    def test_check_button_see_more(self):
        driver.find_elements_by_css_selector("btn btn-light btn--m btn--inline btn-light--link FA8aij")
  
    def test_check_link(self):
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,"Dép")
        driver.find_element(By.LINK_TEXT,"Váy")
        driver.find_element(By.LINK_TEXT,"Áo Phông")
        driver.find_element(By.LINK_TEXT,"Dép Nữ")
        driver.find_element(By.LINK_TEXT,"Đăng Ký")


if __name__ == "__main__":
    unittest.main()