from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests

key_input = input("enter key: ")
# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.alibaba.com//trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText=samsung"

def make_csv(page_url):

    # opens the connection and downloads html page from url
    try:
        uClient = requests.get(page_url).text
        
    except:
        print("Connection failed")
        return

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient, "html.parser")
    # uClient.close()

    # print(page_soup)
    # finds each product from the store page
    containers = page_soup.findAll("div", {"class": "organic-list app-organic-search__list"})

    print(containers)

    # name the output file to write to local disk
    # out_filename = "graphics_cards.csv"
    # header of csv file to be written
    headers = "product_name,price \n"

    # opens file, and writes headers
    f = open(key_input+".csv", "w", encoding="UTF-8")
    f.write(headers)

    # loops over each product and grabs attributes about
    # each product
    for container in containers:
        # Finds all link tags "a" from within the first div.
        make_rating_sp = container.div

        # print(f"a: {make_rating_sp}")

        # Grabs the title from the image title attribute
        # Then does proper casing using .title()
        # brand = make_rating_sp[0].img["alt"].title()

        # Grabs the text within the second "(a)" tag from within
        # the list of queries.
        product_name = container.img["alt"]
        # print(f"product_name: {product_name}")

        # Grabs the product shipping information by searching
        # all lists with the class "price-ship".
        # Then cleans the text of white space with strip()
        # Cleans the strip of "Shipping $" if it exists to just get number
        special_price = container.findAll("div", {"class":""})
        price = special_price[0].select_one("span").text.replace("\n", " ")
        # print(price.replace("\n", " "))
        # prints the dataset to console
        # print("brand: " + brand + "\n")
        print("product_name: " + product_name + "\n")
        print("price: " + price + "\n")

        # writes the dataset to file
        f.write(product_name.replace(",", "|") + ", " + price + "\n")

    f.close()  # Close the file

make_csv(page_url)