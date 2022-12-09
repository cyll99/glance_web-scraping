
from bs4 import BeautifulSoup
import requests

def canez(input_key, file):
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
    page_url = "https://valeriocanez.com/index.php?route=product/search&search="+input_key
    # opens the connection and downloads html page from url
    try:
        # HTTP Request
        webpage = requests.get(page_url, headers=HEADERS)
    except:
        print("Connection failed")
        return

    soup = BeautifulSoup(webpage.content, "html.parser")
    # print(soup)

    results = soup.find_all("div", {"class":"product-layout swiper-slide"})
    # print(results)

	


    with open(file, "a", encoding="UTF-8") as f:
        f.write("Valerio Canez web site \n\n")
 
        for result in results:
            # print(result)
            try:
                name = result.find_all("div", {"class":"name"})
                name = name[0].select_one("a").text.strip()
                # print(name)
            except:
                name = result.find_all("h4")
                name = name[0].select_one("a").text.strip()
			

            
            price = result.find_all("div", attrs={"class":'price'})
            price = price[0].select_one("span").text.strip()
            # print(price)
          

            # writes the dataset to file
            f.write(name.replace(",", "|") + ", " + price + "\n")
        f.write("\n")
        print("Done")


