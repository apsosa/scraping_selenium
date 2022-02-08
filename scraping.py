import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)


#import ipdb;ipdb.set_trace()
driver.get('https://www.starz.com/ar/es/movies')

time.sleep(5) # Let the user actually see something!

#search_box = driver.find_element_by_name('q')
import ipdb;ipdb.set_trace()

search_box = driver.find_element(By.CSS_SELECTOR, 'div.text-uppercase')


#import ipdb;ipdb.set_trace()
