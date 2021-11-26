import requests
from bs4 import BeautifulSoup
import json
url='https://www.imdb.com/india/top-rated-indian-movies/'

# step 1: get the html
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

# step 2: parse the html
soup=BeautifulSoup(htmlContent,"html.parser")

def scrape_movie():
    main_div=soup.find("div", class_="lister")
    # print(main_div)
    tbody=main_div.find("tbody",class_="lister-list")
    table_raws=tbody.find_all("tr")
    movie_list=[]
    s=1
    for tr in table_raws:
        # position=tr.find('td',class_="titleColumn").get_text().strip()
        name = tr.find("td",class_="titleColumn").a.get_text()
        year=tr.find("td",class_="titleColumn").span.get_text()
        rating=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url=tr.find("td","titleColumn").a['href']
        movie_link="https://www.imdb.com"+url
        Details={"position":"","Name":"","Year":"","Rating":"","URL":""}
        Details["position"]=s
        s=s+1
        Details["Name"]=name
        Details["Year"]=int(year[1:5])
        Details["Rating"]=float(rating)
        Details["URL"]=movie_link
       
        movie_list.append(Details.copy())
        with open("Task1.json","w") as file:
            json.dump(movie_list,file,indent=4)
    return movie_list

(scrape_movie())