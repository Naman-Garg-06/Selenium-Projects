from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/naman/Downloads/chromedriver')
#driver.set_page_load_timeout(10)
driver.get('https://www.facebook.com/')
driver.find_element_by_xpath('//*[@id="email"]').send_keys('garg.naman0607@gmail.com')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('******')
driver.find_element_by_id("u_0_2").click()
driver.find_element_by_xpath('//*[@id="userNavigationLabel"]').click()
driver.findElement_by_id('u_d_1').click()
time.sleep(4)
driver.close()
