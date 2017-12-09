from selenium import webdriver
import time
driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://sadfasdf/phone_login?keep_login=false')
print(driver.get_cookies())

driver.find_element_by_id('input_local_phone_number').send_keys('1')
driver.find_element_by_id('input_password').send_keys('**')
# 로그인 버튼을 눌러주자.
driver.find_element_by_class_name("uBtn").click()
time.sleep(5);
driver.find_element_by_class_name("uBtn").click()



