import requests
import urllib.request
from bs4 import BeautifulSoup
import csv

URL="https://store.musinsa.com/app/items/lists/002017/?category=&d_cat_cd=002017&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90"

def get_last_page():
    result=requests.get(URL)
    soup=BeautifulSoup(result.text,"html.parser")
    last_page=soup.find("span",{"class":"pagingNumber"}).find("span",{"class":"totalPagingNum"}).get_text().strip()
    print(f"이 카테고리는 {last_page}페이지 까지 있습니당")
    return int(last_page)

def get_image(max_page):
    for page in range(max_page):
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        images=soup.find_all("li",{"class":"li_box"})
        print(f"{page+1}페이지 긁어오는중~~~\n")
        for img in images:
            image=img.find("div",{"class":"list_img"}).find("a").get("href")
            # 상세페이지 태그
            imgurl=f"https://store.musinsa.com{image}"
            res=requests.get(imgurl)
            sp=BeautifulSoup(res.text,"html.parser")
            highresolImg=sp.find("div",{"class":"product-img"}).find("img")
            # 상세페이지의 대표 상품 이미지
            imgURL=highresolImg.get("src")
            imgName=highresolImg.get("alt")
            urllib.request.urlretrieve("https:"+imgURL,(imgName+".jpg").replace("/"," "))
            #이미지 저장시 상품명에 '/'포함시 디렉토리 경로로 인식함ㅠ->/를 space로 대체
#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트


def save_to_file(infos):
    file=open("infos.csv",mode="w",encoding='utf-8',newline='')
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
        #페이지 별로 긁어오기(for~range니까 +1한 값으로 이동되게)
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
        print(f"{page+1}페이지 긁어오는중~~~\n")
    save_to_file(list)
    return list

save_to_file(get_items(get_last_page()))
get_image(get_last_page())

