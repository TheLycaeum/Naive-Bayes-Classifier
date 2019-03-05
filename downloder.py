import requests
import bs4 #for pulling data out of HTML and XML files
import os
import re

url = input("Enter your URL here: ")
def downlod_lyrics(url):
    """downlod lyrics form url and return as string format"""
    res = requests.get(url)
    data = bs4.BeautifulSoup(res.text, 'lxml')
    folder_name = data.find("div", class_="grid_6 suffix_6").h1.text
    os.mkdir(f"/home/fairoos/naive_byaes/training_data/{folder_name}")
    body = data.find('div',id ='popular')
    sub_body = body.find('tbody')
       # print(body.prettify())
    for file_names in sub_body.find_all('a',class_="title hasvidtable"):
        file_name =file_names.get('alt')
        link  = file_names.get("href")
        res1 = requests.get(link)
        soup = bs4.BeautifulSoup(res1.text, 'lxml')
        print(file_name)
        print(link)
        lyrics = " "
        for i in soup.select('.verse'):
            lyrics += i.text
        filepath = os.path.join(f"/home/fairoos/naive_byaes/training_data/{folder_name}", file_name)
        fil = open(filepath, 'w')
        fil.write(lyrics)
        fil.close()
downlod_lyrics(url)
