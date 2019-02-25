import requests
import bs4 #for pulling data out of HTML and XML files

url = input("Enter your URL here: ")
def downlod_file(url):
    res = requests.get(url)
    data = bs4.BeautifulSoup(res.text, 'lxml')
    lyrics = " "
    for i in data.select('.verse'):
        lyrics += i.text
    return  lyrics
    
print(downlod_file(url))
