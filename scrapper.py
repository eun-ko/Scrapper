import requests
import urllib.request
from bs4 import BeautifulSoup

URL="https://store.musinsa.com/app/items/lists/022/?category=&d_cat_cd=022&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90"

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
        for i in img:
            imgUrl=i["data-original"]
            print("https:"+imgUrl)
            urllib.request.urlretrieve("https:"+imgUrl,i["alt"]+'.jpg')


def get_items(max_page):
    brandlist=[]
    itemlist=[]
    pricelist=[]
    for page in range(max_page):
        #페이지 별로 긁어오기(0~9인데 +1한 값으로 이동되게)
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        brandName=soup.select("#searchList > li > div.li_inner > div.article_info > p.item_title")
        itemName=soup.select("#searchList > li > div.li_inner > div.article_info > p.list_info > a")
        price=soup.select("#searchList > li > div.li_inner > div.article_info > p.price")
        #select의 결과는 list의 형태임 find_all과 같은 메소드
        
        for i in range(len(itemName)):
            itemlist.append(itemName[i].get_text(strip=True))
        for i in range(len(brandName)):
            brandlist.append(brandName[i].get_text(strip=True))
        for i in range(len(price)):
            delprice=price[i].find("del")
            #price리스트의 원소 하나하나에 del태그를 따로 변수에 저장
            if delprice:
                #그 태그가 존재하면
                delprice.extract()
                #그 태그를 없애기..price[i]안에서 없어지는건가?
            pricelist.append(price[i].get_text(strip=True))
    print(pricelist)


get_items(get_last_page())
get_image(get_last_page())
