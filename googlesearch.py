from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/naman/Downloads/chromedriver')
#driver.set_page_load_timeout(10)
driver.get('https://www.google.com/')
driver.find_element_by_name('q').send_keys("How's the Josh"+"\n")
time.sleep(4)
driver.close()