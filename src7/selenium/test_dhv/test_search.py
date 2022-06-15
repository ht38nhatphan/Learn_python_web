from logging import error
import os
import pathlib
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# values for drowdown
driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):
    def setUp(self):
        driver.get("http://student.vinhuni.edu.vn/")
    
    def test_title(self):
        self.assertEqual(driver.title, ".: Đăng nhập :.")
    
    def test_check_radio_button(self):
        driver.find_element_by_id("PageHeader1_chkNgonNgu")
        

    def test_switch_language(self):
        select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "PageHeader1_drpNgonNgu"))))
        select.select_by_visible_text("VN")
        # select.select_by_visible_text("EN")
        driver.find_element(By.LINK_TEXT,"Home")
        


if __name__ == "__main__":
    unittest.main()