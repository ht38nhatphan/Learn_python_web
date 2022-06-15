import os
import pathlib
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# gef file path local
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    # def test_title(self):
    #     driver.get("http://student.vinhuni.edu.vn/")
    #     self.assertEqual(driver.title, "")
    # def test_login(self):
    #     driver.get("http://student.vinhuni.edu.vn/")
    #     time.sleep(1)
    #     driver.find_element_by_id("Username").send_keys("admin")
    #     time.sleep(1)
    #     driver.find_element_by_id("Password").send_keys("admin")
    #     time.sleep(0.5)
    #     driver.find_element_by_id("login_submit").click()
    #     time.sleep(0.5)
    #     driver.find_element_by_id("Password").clear()
    #     self.assertEqual(driver.find_element_by_class_name("errorBox").text, "Sai tên đăng nhập hoặc mật khẩu")
    
    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")
    def test_check_butons(self):
        driver.get(file_uri("counter.html"))
        driver.find_element(By.ID,"increase")
    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")
        driver.close()
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

