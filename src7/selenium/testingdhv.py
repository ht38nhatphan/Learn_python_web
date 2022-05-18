from logging import error
import os
import pathlib
import unittest
import time
from selenium import webdriver
import json

# gef file path local
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):
    def setUp(self):
        driver.get("http://student.vinhuni.edu.vn/")

    def test_title(self):
        self.assertEqual(driver.title, ".: Đăng nhập :.")
        time.sleep(1)
        driver.close()
    def test_login_wrong_name_and_pass(self):
        driver.find_element_by_id("txtUserName").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin")
        driver.find_element_by_id("btnSubmit").click()
        driver.find_element_by_id("txtUserName").clear()
        
        
        self.assertEqual(driver.find_element_by_id("lblErrorInfo").text, "Bạn đã nhập sai tên hoặc mật khẩu!")
    def test_login_wrong_name(self):
        driver.find_element_by_name("txtUserName").send_keys("s")
        driver.find_element_by_id("txtPassword").send_keys("asdjsdh")
        
        driver.find_element_by_id("btnSubmit").click()
        self.assertTrue(driver.find_element_by_id("lblErrorInfo").text, "Tên đăng nhập không đúng!")
    def test_login_done(self):
        time.sleep(0.05)
        driver.find_element_by_name("txtUserName").send_keys("18574802010097")
        driver.find_element_by_id("txtPassword").send_keys("0129nhat")
        
        driver.find_element_by_id("btnSubmit").click()
        # driver.find_element_by_id("txtUserName").clear()
        # driver.current_url("http://student.vinhuni.edu.vn/CMCSoft.IU.Web.Info/Home.aspx")
        self.assertTrue(driver.title,".: Hệ thống đăng ký học :.")
        driver.back()
    # def test_dropdown(self):

    # def test_registration(self):


    def test_click_link(self):
        self.assertTrue(driver.title,".: Hệ thống đăng ký học :.")
        driver.back()
    
    def test_logout(self):
        driver.find_element_by_link_text("Trang chủ").click()
        driver.find_element_by_link_text("Thoát").click()
        self.assertTrue(driver.title,".: Đăng nhập :.")
        
    
        




    # def test_
    # def test_next(self):
    #     driver.get(file_uri("counter.html"))
    #     next = driver.find_element_by_id("next")
    #     next.click()
    #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")
    # def test_index(self):
    #     driver.get(file_uri("counter.html"))
    #     index = driver.find_element_by_id("index")
    #     index.click()
    #     self.assertEqual(driver.find_element_by_tag_name("h1").text, "0")
    

if __name__ == "__main__":
    unittest.main()
    driver.close()
