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

    def test_check_form_login(self):
        driver.find_element(By.ID,"txtUserName")
        driver.find_element(By.ID,"txtPassword")
        # self.assertEqual(driver.find_element_by_id("txtPassword").text, "text")

    def test_check_button(self):
        time.sleep(1)
        driver.find_element(By.NAME,"btnSubmit")
        driver.find_element(By.XPATH,"/html/body/form[@id='Form1']/table[@id='tblMain']/tbody/tr/td/div[1]/div[@id='pnlLogin']/table[@class='tableborderLogin']/tbody/tr/td/table[@id='Table2']/tbody/tr[3]/td[2]/input")
    
    def test_check_link(self):
        driver.find_element(By.LINK_TEXT,"[ Quên mật khẩu ]")
        driver.find_element(By.LINK_TEXT,"Trang chủ")
        driver.find_element(By.LINK_TEXT,"Đăng nhập")
        driver.find_element(By.LINK_TEXT,"Hỏi đáp")
        driver.find_element(By.LINK_TEXT,"Trợ giúp")

    def test_check_dropdown(self):
        driver.find_element(By.NAME,"PageHeader1$drpNgonNgu")

if __name__ == "__main__":
    unittest.main()