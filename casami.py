
from bs4 import BeautifulSoup
import requests

def casami(input_key, file):
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
    page_url = "https://casamihaiti.com/index.php?category_id=0&search="+input_key+"&submit_search=&route=product%2Fsearch"
    # opens the connection and downloads html page from url
    try:
        # HTTP Request
        webpage = requests.get(page_url, headers=HEADERS)
    except:
        print("Connection failed")
        return

    soup = BeautifulSoup(webpage.content, "html.parser")

    results = soup.find_all("div", {"class":"product-item-container"})
	


    with open(file, "a", encoding="UTF-8") as f:
        f.write("Casami web site \n\n")
 
        for result in results:
            # print(result)
            try:
                name = result.img["title"]
            except:
                name = result.find_all("h4")
                name = name[0].select_one("a").text.strip()
			

            
            price = result.find_all("div", attrs={"class":'price'})
            price = price[0].select_one("span").text.strip()
          

            # writes the dataset to file
            f.write(name.replace(",", "|") + ", " + price + "\n")
        f.write("\n")
        print("Done")


