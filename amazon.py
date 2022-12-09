
from bs4 import BeautifulSoup
import requests

# Function to extract Product Title


def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigatableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find(
            "span", attrs={'id': 'priceblock_ourprice'}).string.strip()

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find(
                "span", attrs={'id': 'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price


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

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))

    with open(file, "a", encoding="UTF-8") as f:
        f.write("Amazon web site \n\n")

      # Loop for extracting product details from each link
        for link in links_list:

            new_webpage = requests.get(
                "https://www.amazon.com" + link, headers=HEADERS)

            new_soup = BeautifulSoup(new_webpage.content, "lxml")

            name = get_title(new_soup)
            price = get_price(new_soup)

            if price is None:
                continue

            print(name , price)

            f.write(name.replace(",", "|") + ", " + price + "\n")

        f.write("\n")
        print("Done")
