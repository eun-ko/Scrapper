import requests
from bs4 import BeautifulSoup


URL="https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20200513"

def get_last_page():
    result=requests.get(URL)
    soup=BeautifulSoup(result.text,"html.parser")
    paging=soup.find("div",{"class":"paging"})
    links=paging.find_all("a")
    pages=[]
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page=pages[-1]
    return max_page

def extract_newsinfo(last_page):
    articles=[]
    for page in range(last_page):
        result=requests.get(f"{URL}&page={page+1}")
        soup=BeautifulSoup(result.text,"html.parser")
        # results=soup.find("dl").find_all("dt")[1].find("a")
        # results=results.get_text(strip=True)
        results=soup.find_all("dl")
        for result in results:
            article=extract_news(result)
            articles.append(article)
        return(articles)

def extract_news(html):
    # html은 dl태그들의 배열 하나하나
    title=html.find("dt").find("a").find_all("img")
    for t in title:
        if 'alt' in t.attrs:
            title=t.attrs['alt']
    # title=html.find("dt").find("a").find("img")["alt"] 
    # 왜 안됨?
    company=html.find("dd").find("span",{"class":"writing"}).get_text()
    return{"title":title,"company":company}
  
extract_newsinfo(get_last_page())