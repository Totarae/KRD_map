import requests
from bs4 import BeautifulSoup
import pandas

base_url="https://www.realtymag.ru/krasnodarskiy-kray/krasnodar/kvartira/prodazha/page/"

l=[]
for page in range(1,21,1):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    base_url+str(page)
    soup=BeautifulSoup(c,'html.parser')
    all=soup.find_all("div",{"class":"offer-wrapper"})
    for item in all:
        d={}
        d["Price"]=item.find("div",{"class":"offer__price"}).text.replace("₽","руб.")
        d["Price/Square"]=item.find("div",{"class":"offer__price-per-square"}).text.replace("₽/м²","руб./м2")
        d["Address"]=item.find("span",{"class":"offer__location"}).text.replace("\xa0"," ")
        try:
            square=item.find_all("div",{"class":"offer__square"})
            for sponge1 in square:
                d["Square"]=sponge1.find("span",{"class":"offer__square-number"}).text
        except:
            d["Square"]=None
        try:
            d["Live Square"]=item.find("div",{"class":"offer__live-square"}).text.replace("м²","м2")
        except:
            d["Live Square"]=None
        try:
            d["Kitchen Square"]=item.find("div",{"offer__kitchen-square"}).text.replace("м²","м2")
        except:
            d["Kitchen Square"]=None
        try:
            d["Floor"]=item.find("div",{"offer__floor"}).text
        except:
            d["Floor"]=None
        try:
            d["Dealer"]=item.find("div",{"offer__status"}).text
        except:
            d["Dealer"]=None
        try:
            d["District"]=item.find("div",{"offer__sublocality"}).text
        except:
            d["District"]=None

        l.append(d)

len(l)
df=pandas.DataFrame(l)
df.to_csv("Output.csv")