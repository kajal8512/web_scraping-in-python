import requests
from bs4 import BeautifulSoup
import json
import pprint
import time
def pickle_task():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    page=requests.get(url)
    # print(page)
    # html=page.content
    # print(html)
    soup=BeautifulSoup(page.text,"html.parser")
    # print(soup)
    div=soup.find("div",class_="_1gX7")
    # print(div)
    # div=soup.find_all("div",class_="_3RA-")
    # print(div)
    div2=div.span.get_text()
    # print(div2)
    pickle=div2.split(" ")
    # print(pickle)
    split=int(pickle[1])
    # print(split)
    split1=split//32+1
    # print(split1)
    a=[]
    position=1
    i=0
    while i <=split1:
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
        api=requests.get(url)
        # print(api)
        soup=BeautifulSoup(api.text,"html.parser")
        # print(soup)
        main_div=soup.find("div",class_="_3RA-")
        # print(main_div)
        div=main_div.find_all("div",class_="UGUy")
        # print(div)
        pickle_price=main_div.find_all("div",class_="_1kMS")
        # print(pickle_price)
        pickle_link=main_div.find_all("div",class_="_3WhJ")
        # print(pickle_link)
        
        k=0
        while k<len(div):
            # position+=1
            pickle_name=div[k].get_text()
            price=pickle_price[k].get_text()
            link=(pickle_link[k].a["href"])
            dict={"position":position,"pickle_name":pickle_name,"link":link,"price":price}
            a.append(dict)
            position+=1
            k+=1
        i+=1
        with open("pickle_task.json","w") as f:
            json.dump(a,f,indent=4)
       
pickle_task()
