from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests

search = input("Enter search: ")
params = {"q":search}
r = requests.get("http://www.bing.com/images",params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol",{"id":"b_results"})
links = results.findAll("li",{"class":"b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        #   print("Parent: ", item.find("a").parent)   
        print("Summary: ", item.find("a").parent.parent.find("p").text)
        
        children = item.find("h2")
        #   for siblings
        print("Next Sibling of h2: ", children.next_sibling)

        #   for children
        for child in children:
            print("Children: ", child)

        


