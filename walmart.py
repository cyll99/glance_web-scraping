# import requests
# from bs4 import BeautifulSoup as soup

# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
# html = requests.get('https://www.walmart.com/browse/personal-care/hand-soap/1005862_1001719?page=1',headers=header)
# bsobj = soup(html.content,'lxml')
# # print(bsobj)

# product_name = bsobj.findAll('div',{'class':'search-result-product-title gridview'})
# product_rating = bsobj.findAll('span',{'class':'seo-avg-rating'})
# product_reviews = bsobj.findAll('span',{'class':'stars-reviews-count'})
# product_price = bsobj.findAll('div',{'data-automation-id':'product-price'})

# print(product_price)

# for names,rating,reviews,price in zip(product_name,product_rating,product_reviews,product_price):
#     print(f"name: {names.a.span.text.strip()}")
#     # item_ratings.append(rating.text)
#     # item_reviews.append(reviews.text.replace('ratings',''))
#     print(f"price: {price.findAll('span',{'class':'visuallyhidden'})[0].text}")

a = ["43", "67.45", "67"]
b = sorted(a)
print(b, a)