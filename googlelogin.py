from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/naman/Downloads/chromedriver')
#driver.set_page_load_timeout(10)
driver.get('https://www.gmail.co.in')
driver.find_element_by_name('identifier').send_keys('17ucs097@lnmiit.ac.in')
driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('******')
driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
time.sleep(8)
driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div/div[2]/div[2]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="gb_71"]').click()
time.sleep(5)
driver.close()
