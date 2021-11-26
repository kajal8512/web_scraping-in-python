from bs4 import BeautifulSoup
from scrape_indiayear_task2 import group_of_year 
from scrape_indiayear_task2 import scrape_movie
import json
scraped_data=scrape_movie()
movie_by_year=group_of_year(scraped_data)
# print(movie_by_year)
def group_by_decades(movies):
    moviedec={}
    list1=[]
    for year in movies:
        mod=year%10
        decade=year-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
        with open("my_file3.json","w")as file:
            json.dump(moviedec,file,indent=4)
    return moviedec   
group_by_decades(movie_by_year)