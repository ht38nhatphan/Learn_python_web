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

    def test_title(self):
        self.assertEqual(driver.title, "Shopee Việt Nam | Mua và Bán Trên Ứng Dụng Di Động Hoặc Website")
        driver.close()

    # def test_slide(self):
    #     driver.find_element_by_id("yui_3_17_2_1_1654180630049_29").click()
    #     self.assertTrue(driver.find_element_by_class_name("carousel-item active"))
    


    def test_check_form_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-searchbar-input")
    
    def test_check_button_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-svg-icon")

    def test_check_input_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input")



    def test_check_import_input_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input").send_keys("Ao phong")
    
    def test_check_click_search(self):
        driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input").send_keys("Ao phong")
        driver.find_element(By.CLASS_NAME,"shopee-svg-icon")
        self.assertEqual(driver.find_elements_by_css_selector("shopee-search-user-brief__header-text-highlight"),"Ao phong")
        driver.back()
    def test_card(self):
        driver.find_element(By.CLASS_NAME,"cart-drawer-container")




    

    

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


    def test_check_categories_detail(self):
        #check image in categories
        driver.find_elements_by_css_selector("H8mXLe")
        #check name in categories
        driver.find_elements_by_css_selector("C9kwfl")  

    def test_check_categories(self):
        driver.find_elements_by_css_selector("_1l+Pw-")
    

    def test_check_flash_sale(self):
        driver.find_elements_by_css_selector("flash-sale-item-card flash-sale-item-card--home-page flash-sale-item-card--VN")

    def test_check_flash_sale_detail(self):
        # % sale
        driver.find_elements_by_css_selector("_5ICO3M yV54ZD X7gzZ7 shopee-badge")
        # image product sale 
        driver.find_elements_by_css_selector("flash-sale-item-card__image flash-sale-item-card__image--home-page")
        # price product sale
        driver.find_elements_by_css_selector("flash-sale-item-card__lower-wrapper flash-sale-item-card__lower-wrapper--VN flash-sale-item-card__lower-wrapper--home-page")
    

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


    def test_check_link_trending_search(self):
        driver.find_elements_by_css_selector("VBhad7 EMJVDR")

    def test_check_trending_search_describe(self):
        #name trending search
        driver.find_elements_by_css_selector("TJqTzh")
        #image trending search
        driver.find_elements_by_css_selector("n-CE6j uibmBH")
    


    def test_check_top_product(self):
        driver.find_elements_by_css_selector("image-carousel__item")
    
    def test_check_top_product_detail(self):
        #image top product
        driver.find_elements_by_css_selector("n-CE6j _06bq+d")
        #name top product
        driver.find_elements_by_css_selector("cXODCZ")
    
    


if __name__ == "__main__":
    unittest.main()