from tqdm import tqdm # tqdm is a smart progress meter
import requests
import bs4 #for pulling data out of HTML and XML files

file_name = input("Enter your song's name: ")
url = input("Enter your URL here: ")
def downlod_file(url, file_name):
    chunk_size = 1024
    res = requests.get(url)
    lyrics = bs4.BeautifulSoup(res.text, 'lxml')
    for i in lyrics.select('.verse'):
        total_size = int(res.headers['content-length'])  
        with open(file_name, 'wb') as f:
            for data in tqdm(iterable = res.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
                f.write(data)

            print("Download completed!")
        return  print(i.text)
    
downlod_file(url, file_name)
