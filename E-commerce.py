import requests
from bs4 import BeautifulSoup
import json
import pprint
import time
url="https://webscraper.io/test-sites"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")
# pprint.pprint(soup)
def scrape_ecommerce():
    main_div=soup.find("div",class_="container test-sites")
    second_div=main_div.find_all("div",class_="col-md-7 pull-right")
    commerce=[]
    k=1
    for i in second_div:
        head=i.find("h2",class_="site-heading").a.get_text().strip()
        link=i.find("h2",class_="site-heading").a["href"]
        E_link="https://webscraper.io/test-sites"+link
        Details={"position":"","Name":"","URL":""}
        Details["position"]=k
        k+=1
        Details["Name"]=head
        Details["URL"]=E_link

        commerce.append(Details.copy())
        with open("E-commerce_task.json","w") as file:
            json.dump(commerce,file,indent=4)
    return commerce
scrape_ecommerce()   

        

