import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

website= "https://www.starz.com/ar/es/movies"
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)

from selenium import webdriver

website= "https://www.starz.com/ar/es/movies"
path= "./chromedriver"


#import ipdb;ipdb.set_trace()
driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

#search_box = driver.find_element_by_name('q')

search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
#import ipdb;ipdb.set_trace()
