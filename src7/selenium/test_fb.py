from logging import error
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
class FacebookWeb(unittest.TestCase):
    def setUp(self):
        driver.get("https://www.facebook.com/")
    def test_title(self):
        self.assertEqual(driver.title, "Facebook – log in or sign up")
    def test_link_create_Account(self):
        driver.find_element(By.LINK_TEXT,"Create New Account")
    
    def test_click_on_create_Account(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        driver.find_elements_by_css_selector("mbs _52lq fsl fwb fcb")

    def test_check_close_signup(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        driver.find_elements_by_css_selector("_8idr img")

    def test_check_card_input(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        driver.find_elements_by_css_selector("inputtext _58mg _5dba _2ph-")
    
    def test_check_dropdown(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        driver.find_elements_by_css_selector("_9407 _5dba _9hk6 _8esg")
    
    def test_check_radio_button(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        driver.find_elements_by_css_selector("_58mt")

    def test_check_button_signup(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        driver.find_elements_by_css_selector("_6j mvm _6wk _6wl _58mi _3ma _6o _6v")
    
    def test_check_import_input_form(self):
       
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        time.sleep(1)
        driver.find_element_by_name("firstname").send_keys("abc")
        driver.find_element_by_name("lastname").send_keys("xyz")
        driver.find_element_by_name("reg_email__").send_keys("ds@gmail.com")
        driver.find_element_by_name("reg_passwd__").send_keys("123456")
        

    
    def test_check_choose_dropdown_form(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        time.sleep(1)
        driver.find_element_by_name("birthday_day").send_keys("1")
        driver.find_element_by_name("birthday_month").send_keys("1")
        driver.find_element_by_name("birthday_year").send_keys("2000")

    
    def test_check_choose_radio_button_form(self):
        driver.find_element(By.LINK_TEXT,"Create New Account").click()
        time.sleep(1)
        driver.find_element_by_css_selector("input[type='radio'][value='1']").click()

        
    



if __name__ == "__main__":
    unittest.main()