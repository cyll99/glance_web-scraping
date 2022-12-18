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



# import re
# from bs4 import BeautifulSoup
# import requests


# def amazon(key_input, file):
#     # Headers for request
#     HEADERS = ({'User-Agent':
#                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
#                 'Accept-Language': 'en-US'})
#     page_url = "https://www.amazon.com/s?k="+key_input
#     # opens the connection and downloads html page from url
#     try:
#         # HTTP Request
#         webpage = requests.get(page_url, headers=HEADERS)
#     except:
#         print("Connection failed")
#         return

#     soup = BeautifulSoup(webpage.content, "html.parser")

#     results = soup.find_all("div", {"data-component-type":"s-search-result"})
#     # results = soup.find_all(re.compile("s-search-result"))
#     # print(len(results))


#     with open(file, "a", encoding="UTF-8") as f:
#         f.write("Amazon web site \n\n")
 
#         for result in results:
#             price = result.find_all("span", attrs={'class':'a-price'})
#             if len(price) == 0:
#                 continue

#             price = price[0].select_one("span").text
            
#             name = result.find_all("span", attrs={"class":'a-size-medium a-color-base a-text-normal'})
#             name = name[0].text
          

#             # writes the dataset to file
#             f.write(name.replace(",", "|") + ", " + price + "\n")
#         f.write("\n")
#         print("Done")







# # Function to extract Product Title
# def get_title(soup):
	
# 	try:
# 		# Outer Tag Object
# 		title = soup.find("span", attrs={"id":'productTitle'})

# 		# Inner NavigatableString Object
# 		title_value = title.string

# 		# Title as a string value
# 		title_string = title_value.strip()

# 	except AttributeError:
# 		title_string = ""	

# 	return title_string

# # Function to extract Product Price
# def get_price(soup):

# 	try:
# 		price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

# 	except AttributeError:

# 		try:
# 			# If there is some deal price
# 			price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

# 		except:		
# 			price = ""	

# 	return price


# # Function to extract Number of User Reviews



# def amazone(key_input, file)

# 	# Headers for request
# 	HEADERS = ({'User-Agent':
# 	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
# 	            'Accept-Language': 'en-US'})

# 	# The webpage URL
# 	URL = "https://www.amazon.com/s?k="+key_input
	
# 	# HTTP Request
# 	webpage = requests.get(URL, headers=HEADERS)

# 	# Soup Object containing all data
# 	soup = BeautifulSoup(webpage.content, "lxml")

# 	# Fetch links as List of Tag Objects
# 	links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

# 	# Store the links
# 	links_list = []

# 	# Loop for extracting links from Tag Objects
# 	for link in links:
# 		links_list.append(link.get('href'))


# 	# Loop for extracting product details from each link 
# 	for link in links_list:

# 		new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

# 		new_soup = BeautifulSoup(new_webpage.content, "lxml")
		
# 		# Function calls to display all necessary product information
# 		print("Product Title =", get_title(new_soup))
# 		print("Product Price =", get_price(new_soup))
	
# 		print()