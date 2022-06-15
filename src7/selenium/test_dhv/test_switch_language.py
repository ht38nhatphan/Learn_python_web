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
    
    


    def test_check_input_search(self):
        time.sleep(0.05)
        driver.find_element_by_name("txtUserName").send_keys("18574802010097")
        driver.find_element_by_id("txtPassword").send_keys("0129nhat")
        
        driver.find_element_by_id("btnSubmit").click()
        
        driver.find_element_by_id("txtsearch").send_keys("aaaaa")
        driver.find_element_by_id("linkTimkiem").click()

        element = driver.find_element_by_class_name("important_newss")





if __name__ == "__main__":
    unittest.main()