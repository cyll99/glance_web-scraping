from bs4 import BeautifulSoup
import requests

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

    soup = BeautifulSoup(webpage.content, "lxml")
    # print(soup)

    results = soup.find_all("div", {"data-component-type":"s-search-result"})


    with open(file, "a", encoding="UTF-8") as f:
 
        for result in results:
            price = result.find_all("span", attrs={'class':'a-price'})
            if len(price) == 0:
                continue

            price = price[0].select_one("span").text
            
            name = result.find_all("span", attrs={"class":'a-size-medium a-color-base a-text-normal'})
            try:
                name = name[0].text.replace(",", "|")
            except:
                print("Not found")
            
            image = result.img["src"].strip()


            # writes the dataset to file
            f.write(f"{image}, {name}, {price}, Amazon\n")
        print("Done")


