#import os,sys
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import CHROME_DRIVER_PATH,RESPONSIVE_URL

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#로드 느린것들 대기

class SearchBot():

  def __init__(self,keyword):
    self.driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    self.keyword=keyword

  def start_search(self):
    self.driver.get("https://google.com")
    search_bar=self.driver.find_element_by_class_name("gLFyf") #결과 첫 요소
    search_bar.send_keys(self.keyword)
    search_bar.send_keys(Keys.ENTER) 
    #send_keys는 키보드 인풋만 가능. 변수 전달 x
    elements_to_exclude=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"g-blk")))
    #element 위치 생길때까지 wait , 필요없는 요소(첫페이지에만 등장) 삭제
    pagination=self.driver.find_elements_by_tag_name("td")
    del pagination[0:2]
    flag=True
    #첫페인지 판별
    for pagination_index,p in enumerate(pagination):
      if flag:
        self.driver.execute_script("""
        const exclude=arguments[0];
        exclude.parentElement.removeChild(exclude);""",elements_to_exclude)
        flag=False
      search_results_wrapper=self.driver.find_elements_by_class_name("g")
      for index,search_result in enumerate(search_results_wrapper):
        search_result.screenshot(f"screenshots/{self.keyword}_{pagination_index+1}_{index+1}.png")
      p.click()



Google=SearchBot("ewha")
Google.start_search()
#테스트





