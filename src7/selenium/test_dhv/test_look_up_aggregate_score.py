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
        time.sleep(0.05)
        driver.find_element_by_name("txtUserName").send_keys("18574802010097")
        driver.find_element_by_id("txtPassword").send_keys("0129nhat")
    
        driver.find_element_by_id("btnSubmit").click()
        driver.find_element(By.LINK_TEXT,"Tra cứu điểm tổng hợp").click()
        self.assertEqual(driver.title, ".: Tra cứu điểm học tập :.")
        

    def test_check_link(self):
        time.sleep(0.05)
        driver.find_element_by_name("txtUserName").send_keys("18574802010097")
        driver.find_element_by_id("txtPassword").send_keys("0129nhat")

        driver.find_element_by_id("btnSubmit").click()
        driver.find_element(By.LINK_TEXT,"Tra cứu điểm tổng hợp")

    def test_check_form(self):
        time.sleep(0.05)
        driver.find_element_by_name("txtUserName").send_keys("18574802010097")
        driver.find_element_by_id("txtPassword").send_keys("0129nhat")
    
        driver.find_element_by_id("btnSubmit").click()
        driver.find_element(By.LINK_TEXT,"Tra cứu điểm tổng hợp").click()
        driver.find_element_by_id("btnView").click()

        driver.find_elements_by_css_selector("drpStudent")
        driver.find_elements_by_css_selector("drpStudyYear")
        driver.find_elements_by_css_selector("drpSemester")
        driver.find_elements_by_css_selector("btnView")

    def test_click_showform(self):
        time.sleep(0.05)
        driver.find_element_by_name("txtUserName").send_keys("18574802010097")
        driver.find_element_by_id("txtPassword").send_keys("0129nhat")
    
        driver.find_element_by_id("btnSubmit").click()
        driver.find_element(By.LINK_TEXT,"Tra cứu điểm tổng hợp").click()
        driver.find_element_by_id("btnView").click()
        driver.find_elements_by_css_selector("tableBorderMarkView")
    
    
    

        


if __name__ == "__main__":
    unittest.main()