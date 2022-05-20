from cgitb import text
from bs4 import BeautifulSoup
import requests
import pprint
import datetime
import json
import csv


main_data=[]

for r in range(1,6):

    url="https://www.ndtv.com/india/page-"+str(r)
    data= requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    main= soup.find("div",class_="lisingNews")
    news=main.find("div",class_="news_Itm")

    image=[]
    for img in main.findAll("div",class_="news_Itm-img"):
        image.append(img.find("a").img["src"])

    
        # data1["img_url"]=img.find("a").img["src"]

    hading=[]    
    for hdng in main.findAll("h2", class_="newsHdng"):
        hading.append(hdng.text.strip())
        # data1["heading"]=hdng.text.strip()


    ownr=[]
    for owner in main.findAll("span",class_="posted-by"):
        ownr.append(owner.find("a").text.strip())
        # data1["owner_name"]=owner.find("a").text.strip()


    dt=[]
    for date in main.findAll("span",class_="posted-by"):
        dt.append(date.get_text().strip())
        # data1["date"]=date.get_text().strip()


    dtl=[]
    for detail in main.findAll("p",class_="newsCont"):
        dtl.append(detail.text)
        # data1["detail"]=detail.text
    # print(data1)

    for i in range(len(dtl)):
        data1={}
        data1["imageurl"]=image[i]
        data1["heading"]=hading[i]
        data1["ownername"]=ownr[i]
        data1["date"]=dt[i]
        data1["details"]=dtl[i]

        main_data.append(data1)


    pprint.pprint(main_data)

    with open("news.json",'w') as file:
        json.dump(main_data,file,indent=2)
