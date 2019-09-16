from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()

driver.get('http://39.107.96.138:3000/signin')
# 删除帖子
driver.implicitly_wait(20)
driver.find_element_by_id('name').send_keys('user1')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_css_selector('div>input[type="submit"]').click()
driver.maximize_window()
driver.find_element_by_css_selector('a[class="topic_title"]').click()
driver.find_element_by_css_selector('i[class="fa fa-lg fa-trash"]').click()
driver.switch_to_alert
print('text=',Alert(driver).text)
Alert(driver).accept()
driver.back()
driver.refresh()
time.sleep(3)
driver.quit()
