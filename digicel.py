from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests


def digicel(key_input, file):

    page_url = "https://shop.digicelgroup.com/jm/catalogsearch/result/?q="+key_input
    # opens the connection and downloads html page from url
    try:
        uClient = requests.get(page_url).text
    except:
        print("Connection failed")
        return


    page_soup = soup(uClient, "html.parser")

    containers = page_soup.findAll("li", {"class": "item product product-item"})

 
    with open(file, "a", encoding="UTF-8") as f:
 
        for container in containers:

     
            product_name = container.img["alt"].replace(",", "|")
        
            special_price = container.findAll("div", {"class":"product details product-item-details"})
            price = special_price[0].select_one("span").text.replace("\n", " ")
        
            f.write(f"{product_name}, {price}, Digicel\n")

        print("Done")


