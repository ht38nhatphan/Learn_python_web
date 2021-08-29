import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")
time.sleep(1)
driver.find_element_by_id('email').send_keys('*')
time.sleep(1)
driver.find_element_by_id('pass').send_keys('*')
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(2)
driver.get("https://www.facebook.com/profile.php?id=100041515878437")
time.sleep(1)
driver.execute_script('window.scroll(0,1300)')
for i in range(20):
    time.sleep(3)
    driver.execute_script("document.evaluate('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    time.sleep(1)
    driver.execute_script("document.evaluate('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[9]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    time.sleep(1)
    driver.execute_script("document.evaluate('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]/div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")

time.sleep(3)
driver.quit()
