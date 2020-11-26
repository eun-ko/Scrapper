from selenium import webdriver
from config import CHROME_DRIVER_PATH,RESPONSIVE_URL

import time

driver=webdriver.Chrome(
  executable_path=CHROME_DRIVER_PATH
)
driver.get(RESPONSIVE_URL)
driver.maximize_window() #브라우저 크기 최대치로

browser_width=[320,480,960,1366,1920] #height은 스크롤할거니까 상관X

print(driver.get_window_size()) 
#height확인용

for width in browser_width:
  driver.set_window_size(browser_width,1296)
  time.sleep(5)
