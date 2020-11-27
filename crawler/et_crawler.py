#연습용 

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

from selenium.webdriver.common.action_chains import ActionChains
from config import USER_ID,USER_PW,LOGIN_URL,CHROME_DRIVER_PATH


driver=webdriver.Chrome(
  executable_path=CHROME_DRIVER_PATH
)

#button = driver.find_element_by_class_name("close")
#driver.implicitly_wait(10)
#ActionChains(driver).move_to_element(button).click(button).perform()
#driver.find_element_by_class_name("close").click()
#팝업창 처리 오류

butmatge=[]

def get_list():
  #로그인
  driver.get(LOGIN_URL)
  driver.find_element_by_name("userid").send_keys(USER_ID)
  driver.find_element_by_name("password").send_keys(USER_PW)
  driver.find_element_by_class_name("submit").click()
  for page in range(2):
    driver.get(f"https://everytime.kr/260176/p/{page+1}")
    print(f"page : {page+1}")
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    articles=soup.find_all("p",{"class":"medium"})
    for article in articles:
      print("\n")
      content=article.get_text()
      sub_content=content[:70]
      butmatge.append(sub_content)
      print(sub_content)
  return butmatge

print(get_list())