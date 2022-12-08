
from bs4 import BeautifulSoup
import requests

# # Headers for request
# HEADERS = ({'User-Agent':
#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
#             'Accept-Language': 'en-US'})
    
# URL = "https://www.amazon.com/s?k=samsung&crid=1F7EAPI76KZTY&sprefix=samsung%2Caps%2C522&ref=nb_sb_noss_1"

# # HTTP Request
# webpage = requests.get(URL, headers=HEADERS)

# # Soup Object containing all data
# soup = BeautifulSoup(webpage.content, "html.parser")


# # Fetch links as List of Tag Objects
# results = soup.find_all("div", {"data-component-type":"s-search-result"})

# # Loop for extracting product details from each link 
# for result in results:
#     price = result.find_all("span", attrs={'class':'a-price'})
#     if len(price) == 0:
#         continue

#     print(price[0].select_one("span").text)
    
#     name = result.find_all("span", attrs={"class":'a-size-medium a-color-base a-text-normal'})
#     print(name[0].text)




def amazon(key_input, file):
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
    page_url = "https://www.amazon.com/s?k="+key_input
    # opens the connection and downloads html page from url
    try:
        # HTTP Request
        webpage = requests.get(page_url, headers=HEADERS)
    except:
        print("Connection failed")
        return

    soup = BeautifulSoup(webpage.content, "html.parser")

    results = soup.find_all("div", {"data-component-type":"s-search-result"})


    with open(file, "a", encoding="UTF-8") as f:
        f.write("Amazon web site \n\n")
 
        for result in results:
            price = result.find_all("span", attrs={'class':'a-price'})
            if len(price) == 0:
                continue

            price = price[0].select_one("span").text
            
            name = result.find_all("span", attrs={"class":'a-size-medium a-color-base a-text-normal'})
            name = name[0].text
          

            # writes the dataset to file
            f.write(name.replace(",", "|") + ", " + price + "\n")
        f.write("\n")


