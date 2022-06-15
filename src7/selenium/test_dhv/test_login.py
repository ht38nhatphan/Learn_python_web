from logging import error
import os
import pathlib
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# values for drowdown
dr = "/html/body/form[@id='frmBody']/div[@class='container-home']/div[@class='left-home']/div[@id='left']/div[@class='skin-green-light sidebar-mini']/div[@id='Menu1_div_nav_menu']/ul[@class='sidebar-menu']/li[3]/a"
dr_b = "/html/body/form[@id='frmBody']/div[@class='container-home']/div[@class='left-home']/div[@id='left']/div[@class='skin-green-light sidebar-mini']/div[@id='Menu1_div_nav_menu']/ul[@class='sidebar-menu']/li[@class='active']/ul[@class='treeview-menu menu-open']/li[@class='treeview'][1]/a"
driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):
    def setUp(self):
        driver.get("http://student.vinhuni.edu.vn/")

    def test_login_wrong_name_and_pass(self):
        # time.sleep(5)
        driver.find_element_by_id("txtUserName").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("admin")
        driver.find_element_by_id("btnSubmit").click()
        driver.find_element_by_id("txtUserName").clear()
        
        
        self.assertEqual(driver.find_element_by_id("lblErrorInfo").text, "Bạn đã nhập sai tên hoặc mật khẩu!")
    def test_login_wrong_name(self):
        # time.sleep(5)
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



        


if __name__ == "__main__":
    unittest.main()
