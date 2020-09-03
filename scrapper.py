import requests
import urllib.request
from bs4 import BeautifulSoup
import csv

#URL="https://store.musinsa.com/app/items/lists/002/?category=&d_cat_cd=002&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90"
# 아우터-전체

# URL="https://store.musinsa.com/app/items/lists/001001/?category=&d_cat_cd=001001&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90"
# 상의-반팔

#URL="https://store.musinsa.com/app/items/lists/003/?category=&d_cat_cd=003&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=90"
#하의-전체

URL = "https://display.musinsa.com/display/brands/critic?category2DepthCodes=&category1DepthCode=&colorCodes=&startPrice=&endPrice=&exclusiveYn=&includeSoldOut=&saleGoods=&sortCode=pop&tags="

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
        print(f"{page+1}페이지\n")
        for img in images:
            detail=img.find("div",{"class":"list_img"}).find("a").get("href")
            # 상세페이지 주소
            detailUrl=f"https://store.musinsa.com{detail}"
            res=requests.get(detailUrl)
            sp=BeautifulSoup(res.text,"html.parser")
            highresolImg=sp.find("div",{"class":"product-img"}).find("img")
            # 상세페이지의 대표 상품 이미지
            imgURL=highresolImg.get("src")
            imgName=highresolImg.get("alt")
            urllib.request.urlretrieve("https:"+imgURL,(imgName+".jpg").replace("/"," ").replace("*"," "))
            
#img.alt는 이미지 대체 텍스트

def get_image_by_brand(max_page):
    for page in range(max_page):
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        images=soup.select("#searchList > li > div.li_inner > div.list_img > a")
        print(f"{page+1}페이지\n")
        for img in images:
            detail=img.get("href")
            detailUrl=f"https:{detail}"
            # 상세페이지 주소
            res=requests.get(detailUrl)
            sp=BeautifulSoup(res.text,"html.parser")
            highresolImg=sp.find("div",{"class":"product-img"}).find("img")
            imgURL=highresolImg.get("src")
            imgName=highresolImg.get("alt")
            # print(f"{page+1}페이지 {imgName}")
            urllib.request.urlretrieve("https:"+imgURL,(imgName+".jpg").replace("/"," ").replace("*"," "))

def size_csv(max_page):
    file=open("sizeInfos.csv",mode="w",encoding='utf-8',newline='')
    writer=csv.writer(file)
    writer.writerow(["브랜드","상품이름","상품url","사이즈","총장(cm)","어깨너비(cm)","가슴단면(cm)","소매길이(cm)"])
    for page in range(max_page):
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        detailpage=soup.find_all("li",{"class":"li_box"})
        print(f"{page+1}페이지\n")
        for page in detailpage:
            detail=page.find("div",{"class":"list_img"}).find("a").get("href")
            detailUrl=f"https://store.musinsa.com{detail}"
            res=requests.get(detailUrl)
            sp=BeautifulSoup(res.text,"html.parser")
            item=sp.find("div",{"class":"product-img"}).find("img")
            itemname=item.get("alt")
            brandname=sp.find("p",{"class":"product_article_contents"}).find("a").get_text()
            table=sp.find("table",{"class":"table_th_grey"})
            if table:
                rows=table.find_all("tr")[3:]
                for row in rows:
                    sizeheader=row.find("th").get_text()
                    if sizeheader=="옵션없음":
                        sizeheader="단일사이즈"
                    sizes=row.find_all("td")
                    if len(sizes)==4:
                        length=sizes[0].get_text()
                        shoulder=sizes[1].get_text()
                        chest=sizes[2].get_text()
                        sleeve=sizes[3].get_text()
                        if(row==rows[0]):
                            writer.writerow([brandname,itemname,detailUrl,sizeheader,length,shoulder,chest,sleeve])
                        else:
                            writer.writerow(["","","",sizeheader,length,shoulder,chest,sleeve])
                    elif len(sizes)==3:
                        length=sizes[0].get_text()
                        chest=sizes[1].get_text()
                        sleeve=sizes[2].get_text()
                        if(row==rows[0]):
                            writer.writerow([brandname,itemname,detailUrl,sizeheader,length,"",chest,sleeve])
                        else:
                            writer.writerow(["","","",sizeheader,length,"",chest,sleeve])
            else:
                writer.writerow([brandname,itemname,detailUrl,"사이즈 없음","사이즈 없음","사이즈 없음","사이즈 없음","사이즈 없음"])
                
    return


def bottom_size_csv(max_page):
    file=open("bottom_sizeInfos.csv",mode="w",encoding='utf-8',newline='')
    writer=csv.writer(file)
    writer.writerow(["브랜드","상품이름","상품url","사이즈","총장","허리단면","허벅지단면","밑위","밑단단면"])
    for page in range(max_page):
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        detailpage=soup.find_all("li",{"class":"li_box"})
        print(f"{page+1}페이지\n")
        for page in detailpage:
            detail=page.find("div",{"class":"list_img"}).find("a").get("href")
            detailUrl=f"https://store.musinsa.com{detail}"
            res=requests.get(detailUrl)
            sp=BeautifulSoup(res.text,"html.parser")
            item=sp.find("div",{"class":"product-img"}).find("img")
            itemname=item.get("alt")
            brandname=sp.find("p",{"class":"product_article_contents"}).find("a").get_text()
            table=sp.find("table",{"class":"table_th_grey"})
            if table:
                rows=table.find_all("tr")[3:]
                for row in rows:
                    sizeheader=row.find("th").get_text()
                    sizes=row.find_all("td")
                    if len(sizes)==5:
                        length=sizes[0].get_text()
                        w=sizes[1].get_text()
                        d=sizes[2].get_text()
                        u=sizes[3].get_text()
                        s=sizes[4].get_text()
                        if(row==rows[0]):
                            writer.writerow([brandname,itemname,detailUrl,sizeheader,length,w,d,u,s])
                        else:
                            writer.writerow(["","","",sizeheader,length,w,d,u,s])
                
            if not table:
                writer.writerow([brandname,itemname,detailUrl,"사이즈 없음","사이즈 없음","사이즈 없음","사이즈 없음","사이즈 없음","사이즈 없음"])
    return

def get_items(max_page):
    list=[]
    for page in range(max_page):
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
       
        brandName=soup.select("#searchList > li > div.li_inner > div.article_info > p.item_title > a")
        itemName=soup.select("#searchList > li > div.li_inner > div.article_info > p.list_info > a")
        price=soup.select("#searchList > li > div.li_inner > div.article_info > p.price")

        for i in range(len(price)):     
            delprice=price[i].find("del")
            if delprice:
                delprice.extract()
            infos={"brand-name":brandName[i].get_text(strip=True),"item-name":itemName[i].get_text(strip=True),"price":price[i].get_text(strip=True)}
            list.append(infos)
        print(f"{page+1}페이지\n")
    product_csv(list)
    return list

def product_csv(infos):
    file=open("productInfos.csv",mode="w",encoding='utf-8',newline='')
    writer=csv.writer(file)
    writer.writerow(["brand-name","item-name","price"])
    for info in infos:
        writer.writerow(list(info.values()))
        #list타입으로 변환
    return


# product_csv(get_items(get_last_page()))

#get_image(get_last_page())

get_image_by_brand(get_last_page())

#size_csv(get_last_page())

#bottom_size_csv(get_last_page())