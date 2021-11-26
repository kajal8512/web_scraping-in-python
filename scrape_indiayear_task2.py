from scrape_india_tast1 import scrape_movie
import json
import pprint
scraped_data=scrape_movie()
# print(scraped_data)
def group_of_year(movies):
    year_list=[]
    for i in movies:
        if i["Year"] not in year_list:
            year_list.append(i["Year"])
            movie_dict={i:[]for i in year_list} 
            for i in movies:
                year1=i["Year"]
                for x in movie_dict:
                    if (x)==(year1):
                        movie_dict[x].append(i)
    with open("year_list1_task2.json","w") as file1:
        json.dump(movie_dict,file1,indent=4)
    return movie_dict
group_of_year(scraped_data)