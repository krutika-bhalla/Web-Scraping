from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os

def start_search():
    search = input("Enter Search Item: ")
    params = {"q": search}

    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)


    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text,"html.parser")
    links = soup.findAll("a",{"class":"thumb"})

    for items in links:
        img_obj = requests.get(items.attrs["href"])
        print("Getting: ", items.attrs["href"])
        title = items.attrs["href"].split("/")[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + title, img.format)
        except:
            print("error")
    
    start_search()

start_search()