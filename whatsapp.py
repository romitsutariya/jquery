from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
browser = webdriver.Firefox('/home/kalubha/Downloads/python/jquery/geckodriver') 
browser.get('https://www.twitter.com') 
  
