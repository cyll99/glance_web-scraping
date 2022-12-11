#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as soup


# In[2]:


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


# In[3]:


html = requests.get('https://www.walmart.com/browse/personal-care/hand-soap/1005862_1001719?page=1',headers=header)


# In[4]:


bsobj = soup(html.content,'lxml')


# In[5]:


bsobj


# In[6]:


url_list = []
for i in range(1,26):
    url_list.append('https://www.walmart.com/browse/personal-care/hand-soap/1005862_1001719?page=' + str(i))
url_list


# In[7]:


item_names = []
price_list = []
item_ratings = []
item_reviews = []


# In[8]:


bsobj.findAll('div',{'class':'search-result-product-title gridview'})


# In[9]:


bsobj.findAll('span',{'class':'seo-avg-rating'})


# In[10]:


bsobj.findAll('span',{'class':'price display-inline-block arrange-fit price price-main'})[0].findAll('span',{'class':'visuallyhidden'})[0].text


# In[12]:


bsobj.findAll('span',{'class':'stars-reviews-count'})[0].text.replace('ratings','')


# In[13]:


for url in url_list:
    result = requests.get(url)
    bsobj = soup(result.content,'lxml')
    
    product_name = bsobj.findAll('div',{'class':'search-result-product-title gridview'})
    product_rating = bsobj.findAll('span',{'class':'seo-avg-rating'})
    product_reviews = bsobj.findAll('span',{'class':'stars-reviews-count'})
    product_price = bsobj.findAll('span',{'class':'price display-inline-block arrange-fit price price-main'})
    for names,rating,reviews,price in zip(product_name,product_rating,product_reviews,product_price):
        item_names.append(names.a.span.text.strip())
        item_ratings.append(rating.text)
        item_reviews.append(reviews.text.replace('ratings',''))
        price_list.append(price.findAll('span',{'class':'visuallyhidden'})[0].text)


# In[14]:


# creating a dataframe 
import pandas as pd
df = pd.DataFrame({'Product_Name':item_names, 'Price':price_list, 'Rating':item_ratings,'No_Of_Reviews':item_reviews}, columns=['Product_Name', 'Price', 'Rating', 'No_Of_Reviews'])
df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


r = requests.get('https://www.aliexpress.com/category/708044/graphics-cards.html?spm=a2g0o.home.104.7.650c2145O3Y95j',headers=header)
bsobj2=soup(r.content)
bsobj2

