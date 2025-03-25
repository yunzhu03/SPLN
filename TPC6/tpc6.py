import re
import jjcli
import shelve
import requests
from bs4 import BeautifulSoup as bs

# para não ser banido 
d = shelve.open("pagecache.db")

url = "https://natura.di.uminho.pt/~jj/bs4/folha8-2023/"

def myget(url):
    if url not in d:
        #print(f"... getting {url}")
        d[url] = requests.get(url).text
        #print(d[url])
    return d[url]

def get_article_links():
    txt = myget(url)
    #print(txt)
    dt = bs(txt,'lxml')
    
    links = []

    for tab in dt.find_all("table"):
        for tr in tab.find_all("tr"):
            for td in tr.find_all("td"):
                for a in td.find_all("a"): 
                    links.append(a["href"])
                        
    #print(links)
    return links

def get_article_text(links):
    for link in links:
        print(link)
        txt2 = myget(url+link)
        dtf = bs(txt2,'lxml')
        
        for artigo in dtf.find_all("article"):
            print(artigo.text)
                        

links = get_article_links()
get_article_text(links)
    
d.close()