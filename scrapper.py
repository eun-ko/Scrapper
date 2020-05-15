import requests
import urllib.request
from bs4 import BeautifulSoup
import csv

db={}
URL="https://store.musinsa.com/app/items/lists/015/?category=&d_cat_cd=015&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90"

def get_last_page():
    result=requests.get(URL)
    soup=BeautifulSoup(result.text,"html.parser")
    paging=soup.find("div",{"class":"pagination"}).find("div",{"class":"wrapper"}).find_all("a")
    pages=[]
    for page in paging:
        if page.get_text(strip=True):
            pages.append(int(page.get_text(strip=True)))

    max_page=pages[-1]
    return int(max_page)


def get_image(max_page):
    for page in range(max_page):
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        img=soup.select("#searchList > li > div.li_inner > div.list_img > a > img")
        print(f"scrapping page {page+1}\n")
        for i in img:
            imgUrl=i["data-original"]
            print("https:"+imgUrl)
            urllib.request.urlretrieve("https:"+imgUrl,i["alt"]+'.jpg')
#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트

def save_to_file(infos):
    file=open("infos.csv",mode="w")
    writer=csv.writer(file)
    #open한 파일에 작성할거임
    writer.writerow(["brand-name","item-name","price"])
    for info in infos:
        writer.writerow(list(info.values()))
        #list타입으로 변환
    return

def get_items(max_page):
    list=[]
    for page in range(max_page):
        #페이지 별로 긁어오기(0~9인데 +1한 값으로 이동되게)
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        brandName=soup.select("#searchList > li > div.li_inner > div.article_info > p.item_title")
        itemName=soup.select("#searchList > li > div.li_inner > div.article_info > p.list_info > a")
        price=soup.select("#searchList > li > div.li_inner > div.article_info > p.price")
        #select의 결과는 list의 형태임 find_all과 같은 메소드
        
        for i in range(len(price)):
            delprice=price[i].find("del")
            #price리스트의 원소 하나하나에 del태그를 따로 변수에 저장
            if delprice:
                #그 태그가 존재하면
                delprice.extract()
                #그 태그를 없애기..price[i]안에서 없어지는건가?
            infos={"brand-name":brandName[i].get_text(strip=True),"item-name":itemName[i].get_text(strip=True),"price":price[i].get_text(strip=True)}
            list.append(infos)
        print(f"scrapping page {page+1}\n")
    save_to_file(list)
    return list
        

get_items(get_last_page())
    
