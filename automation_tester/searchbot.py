from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#로드 느린것들 대기

from config import CHROME_DRIVER_PATH,RESPONSIVE_URL

KEYWORD=""

driver=webdriver.Chrome(
  executable_path=CHROME_DRIVER_PATH
)

driver.get("https://google.com")

search_bar=driver.find_element_by_class_name("gLFyf") #결과 첫 요소

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER) 
#send_keys는 키보드 인풋만 가능. 변수 전달 x

elements_to_exclude=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"g-blk")))
#element 위치 생길때까지 wait , 필요없는 요소 삭제

driver.execute_script("""
const exclude=arguments[0];
exclude.parentElement.removeChild(exclude)""",elements_to_exclude)

search_results_wrapper=driver.find_elements_by_class_name("g")

for index,search_result in enumerate(search_results_wrapper):
  search_result.screenshot(f"screenshots/{KEYWORD}_{index+1}.png")
  #class_attribute=search_result.get_attribute("class")
  #if "kno-kp mnr-c g-blk" not in class_attribute:
  #  search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
