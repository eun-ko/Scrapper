from selenium import webdriver
from config import CHROME_DRIVER_PATH,RESPONSIVE_URL

import time
import math

MY_BROWSER_HEIGHT=1296

class ResponsiveAutomation:
  #생성자
  def __init__(self,urls):
    self.driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    self.driver.maximize_window() #브라우저 크기 최대치로
    self.urls=urls
    self.browser_width=[480,960,1366,1920] #height은 스크롤할거니까 상관X

  def start_automation(self):
    for url in self.urls:
      self.get_screenshot(url)
  
  def get_screenshot(self,url):
    self.driver.get(url)
    for width in self.browser_width:
      self.driver.set_window_size(width,MY_BROWSER_HEIGHT)
      self.driver.execute_script("window.scrollTo(0,0)") #맨 위로 이동
      time.sleep(2)
      scroll_size=self.driver.execute_script("return document.body.scrollHeight") 
      #return-파이썬으로 반환됨
      #print(scroll_size/MY_BROWSER_HEIGHT)
      #scroll size/ browser size ==스크롤 횟수
      total_scroll_numbers=math.ceil(scroll_size / MY_BROWSER_HEIGHT)
  
      for scroll_number in range(total_scroll_numbers+1):
        self.driver.execute_script(f"window.scrollTo(0,{(scroll_number)*MY_BROWSER_HEIGHT})")
        self.driver.save_screenshot(f"screenshots/{width}x{scroll_number+1}.png")
        time.sleep(2)


tester=ResponsiveAutomation([RESPONSIVE_URL])
tester.start_automation()
