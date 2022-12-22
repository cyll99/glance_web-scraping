from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests



def ebay(key_input, file):
    page_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw="+key_input
    # opens the connection and downloads html page from url
    try:
        uClient = requests.get(page_url).text
    except:
        print("Connection failed")
        return

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient, "html.parser")

    # finds each product from the store page
    containers = page_soup.findAll("li", {"class": "s-item s-item__pl-on-bottom"})


    with open(file, "a", encoding="UTF-8") as f:
 
        for container in containers:
            make_rating_sp = container.div

         
            product_name = container.div.div.div.div.img["alt"].replace(",", "|")
            image = container.div.div.div.div.img["src"].strip()

      
            shipping = make_rating_sp.findAll("div", {"class":"s-item__detail s-item__detail--primary"})
            price = shipping[0].select_one("span").text

            link_product = container.div.div.a["href"]
            

            # writes the dataset to file
            f.write(f"{image}, {product_name}, {price}, Ebay, {link_product}\n")

        print("Done")


