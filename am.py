# import requests
# from bs4 import BeautifulSoup as soup

# url = "https://www.amazon.com/s?k=samsung&crid=1F7EAPI76KZTY&sprefix=samsung%2Caps%2C522&ref=nb_sb_noss_1"
# # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

# HEADERS = ({'User-Agent':
#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
#             'Accept-Language': 'en-US, en;q=0.5'})
# # opening connection, grabbing the page
# uClient = requests.get(url, HEADERS)

# # page_html = uClient.read()
# # uClient.close()

# page_soup = soup(uClient.content, "lxml")

# # Outer Tag Object
# title = page_soup.find("span", attrs={"class":'a-size-medium-plus a-color-base a-text-normal'})


# print(page_soup.)

# print(f"title: {title}")




from bs4 import BeautifulSoup
import requests

# Function to extract Product Title
def get_title(soup):
	
	try:
		# Outer Tag Object
		title = soup.find("span", attrs={"id":'productTitle'})

		# Inner NavigatableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip()

		# # Printing types of values for efficient understanding
		# print(type(title))
		# print(type(title_value))
		# print(type(title_string))
		# print()

	except AttributeError:
		title_string = ""	

	return title_string

# Function to extract Product Price
def get_price(soup):

	try:
		price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

	except AttributeError:

		try:
			# If there is some deal price
			price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

		except:		
			price = ""	

	return price

# Function to extract Product Rating
def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		
	except AttributeError:
		review_count = ""	

	return review_count

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()

	except AttributeError:
		available = "Not Available"	

	return available	


if __name__ == '__main__':

	# Headers for request
	HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	            'Accept-Language': 'en-US'})

	# The webpage URL
	# URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"
	# URL = "https://www.amazon.com/s?k=ipad&crid=2FSLK2GXJDXWY&sprefix=ip%2Caps%2C289&ref=nb_sb_ss_ts-doa-p_1_2"
	URL = "https://www.amazon.com/s?k=samsung&crid=1F7EAPI76KZTY&sprefix=samsung%2Caps%2C522&ref=nb_sb_noss_1"

	
	# HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "html.parser")
    

	# Fetch links as List of Tag Objects
	links = soup.find_all("div", {"data-component-type":"s-search-result"})
	i = 1


    
    

	# # Store the links
	# links_list = []

	# # Loop for extracting links from Tag Objects
	# for link in links:
    #         name = links.find("span", attrs={'id':'a-size-medium a-color-base a-text-normal'}).string.strip()
    #         price = links.find("span", attrs={'id':'a-offscreen'}).string.strip()
    #         print(name, price)
    #         print("a")


   

 

		# links_list.append(link.get('href'))

    
	# Loop for extracting product details from each link 
	for link in links:
		price = link.find_all("span", attrs={'class':'a-price'})
		if len(price) == 0:
		    continue
  
		print(price[0].select_one("span").text)
        
		name = link.find_all("span", attrs={"class":'a-size-medium a-color-base a-text-normal'})
		print(name[0].text)
		

		
		
		# Function calls to display all necessary product information
		# print("Product Title =", name)
		# print("Product Price =", price)
		# print("Product Rating =", get_rating(new_soup))
		# print("Number of Product Reviews =", get_review_count(new_soup))
		# print("Availability =", get_availability(new_soup))
	# 	print()