from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time
from config import CHROME_DRIVER_PATH

import win32com.client as comclt

driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
wsh= comclt.Dispatch("WScript.Shell")
used_hashtags=[]

def wait_for(locator):
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))

def login():
  driver.get("https://www.instagram.com")
  id=wait_for((By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input"))
  pw=wait_for((By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input"))
  id.send_keys(input("ID:"))
  pw.send_keys(input("PW:"),Keys.ENTER)
  login_info=wait_for((By.XPATH,"//*[@id='react-root']/section/main/div/div/div/div/button"))
  login_info.click()
  notification_btn=wait_for((By.XPATH,"/html/body/div[4]/div/div/div/div[3]/button[2]"))
  notification_btn.click()

def extract_infos(hashtag):
  search_bar=wait_for((By.XPATH,"//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input"))
  search_bar.send_keys(hashtag)
  time.sleep(1)
  related_hashtags=driver.find_elements_by_class_name("yCE8d")
  for related_hashtag in related_hashtags[:10]:
    time.sleep(1)
    ActionChains(driver).move_to_element(related_hashtag).context_click().perform()
    #ActionChain 동시에 수행
    wsh.SendKeys("{DOWN}")
    wsh.SendKeys("{ENTER}")
    used_hashtags.append(related_hashtag.text.replace("\n","_"))
  used_hashtags.reverse()
  driver.set_window_size(430,900)
  for i,window in enumerate(driver.window_handles):
    driver.switch_to.window(window)
    if i!=0:
      grid_img=wait_for((By.XPATH,"//*[@id='react-root']/section/main/article/div[1]/div"))
      driver.execute_script("window.scrollTo(0, 150)")
      grid_img.screenshot(f"screenshots/{hashtag}_{used_hashtags[i-1]}.png")
      #첫 window(i==0)는 내 피드. 인덱스-1 주의

login()
extract_infos("#corona")