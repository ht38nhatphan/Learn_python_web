from logging import error
import os
import pathlib
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# gef file path local
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):
    def setUp(self):
        driver.get("http://elearning.vinhuni.edu.vn/")

    def test_title(self):
        self.assertEqual(driver.title, "VinhUni E-Learning")
        driver.close()

    # def test_slide(self):
    #     driver.find_element_by_id("yui_3_17_2_1_1654180630049_29").click()
    #     self.assertTrue(driver.find_element_by_class_name("carousel-item active"))
    
    def test_check_form_search(self):
        driver.find_element(By.NAME,"search")

    def test_check_button(self):
        time.sleep(1)
        driver.find_element_by_xpath("/html[@class='yui3-js-enabled mdl-js']/body[@id='page-site-index']/header[@id='header']/div[@class='container navbar-nav']/div[1]/button[@class='btn pull-xs-left m-r-1 btn-secondary']/span[4]")
        #driver.find_element(By.XPATH,"/html[@class='yui3-js-enabled mdl-js']/body[@id='page-site-index']/header[@id='header']/div[@class='container navbar-nav']/div[1]/button[@class='btn pull-xs-left m-r-1 btn-secondary']")
    
    def test_check_link(self):
        time.sleep(1)
        # driver.find_element(By.PARTIAL_LINK_TEXT,"Trang chủ ")
        driver.find_element(By.LINK_TEXT,"Trang cá nhân")
        driver.find_element(By.LINK_TEXT,"Khóa học")
        driver.find_element(By.LINK_TEXT,"Hướng dẫn sử dụng")

    # def test_check_dropdown(self):
    #     driver.find_element(By.NAME,"PageHeader1$drpNgonNgu")

    def test_import_search(self):
        driver.find_element(By.NAME,"search").send_keys("học viện")
    
    def test_check_click_search(self):
        time.sleep(1)
        driver.find_element(By.XPATH,"/html[@class='yui3-js-enabled mdl-js']/body[@id='page-site-index']/div[@class='header-main']/div[@class='header-main-content']/div[@class='container']/div[@class='top-search']/form/input[2]").click()
        driver.find_element(By.ID,"region-main-box")
        driver.back()
    
    def test_check_search_sussedfull(self):
        
        driver.find_element(By.NAME,"search").send_keys("học viện")
        driver.find_element(By.XPATH,"/html[@class='yui3-js-enabled mdl-js']/body[@id='page-site-index']/div[@class='header-main']/div[@class='header-main-content']/div[@class='container']/div[@class='top-search']/form/input[2]").click()
        driver.find_element(By.XPATH,"/html[@class='yui3-js-enabled mdl-js']/body[@id='page-course-search']/div[@id='page-wrapper']/div[@class='header-main']/div[@id='page']/div[@id='page-content']/div[@id='region-main-box']/section[@id='region-main']/div[@class='card card-block']/div/h2")
        driver.back()
    
    def test_check_logo(self):
        driver.find_element_by_xpath("/html[@class='yui3-js-enabled mdl-js']/body[@id='page-site-index']/div[@id='yui_3_17_2_1_1654977684042_31']/div[@id='yui_3_17_2_1_1654977684042_30']/div[@id='yui_3_17_2_1_1654977684042_29']/div[@id='logo']/div[@class='col-md-2 col-sm-12']/a[@class='navbar-brand has-logo']").click()
#check slide web page selenium
    

if __name__ == "__main__":
    unittest.main()