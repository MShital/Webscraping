# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:25:22 2017

@author: admin
"""

import requests
import beautifulsoup4
from bs4 import BeautifulSoup
r=requests.get("http://www.amazon.in/product-reviews/B01NAKTR2H/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&refRID=7Z5Z0RCDKVC7WEQ6G9B8&pageNumber=2")
r.content

soup=BeautifulSoup(r.content)
print(soup.prettify)
##block where only comments will be there

 amazon_data=soup.find_all("div",{"class":"a-fixed-right-grid-col a-col-left"})
 
 ###get user names
amazon_data1=soup.find_all("a",{"class":"a-size-base a-link-normal author"})    
 amazon_data1
 
 <a class=""
 
 ----------
import sklearn
sklearn.__version__
sklearn.__version__\
'0.18.1'
from sklearn.linear_model import LinearRegression

#calculate the variance
 import numpy as np
 print(np.var(x,ddof=1))