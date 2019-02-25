from tqdm import tqdm
"""tqdm is a smart progress meter""" 
import requests

file_name = input("Enter your song's name: ")
url = input("Enter your URL here: ")
def downlod_file(url, file_name):
    chunk_size = 1024
    r = requests.get(url, stream = True)
    total_size = int(r.headers['content-length'])
    
    with open(file_name, 'wb') as f:
        for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
            f.write(data)

    print("Download completed!")

    
downlod_file(url, file_name)
