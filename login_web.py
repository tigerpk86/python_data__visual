from selenium import webdriver

driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://asdf/phone_login?keep_login=false')
print(driver.get_cookies())

driver.find_element_by_id('asdf').send_keys('a')
driver.find_element_by_id('asdf').send_keys('a')
# 로그인 버튼을 눌러주자.
#driver.find_element_by_class_name("uBtn").click()



