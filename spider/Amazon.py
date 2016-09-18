# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:26:02 2016

@author: Allen
"""

from bs4 import BeautifulSoup
from urllib import request
import uuid
import datetime
def getAmazonReviewPage(asin,pageNo):
    url1='https://www.amazon.com/product-reviews/'
    url2='/ref=cm_cr_arp_d_paging_btm_1?ie=UTF8&pageSize=50&sortBy=recent&pageNumber='
    #pageNo='1'
    #asin='B00MQSMEEE'
    url=url1+asin+url2+str(pageNo)
    print('url:'+url)
    url='https://www.amazon.com/product-reviews/B00MQSMEEE/ref=cm_cr_arp_d_paging_btm_1?ie=UTF8&pageNumber=1&pageSize=50&sortBy=recent'
    
    #creat http header
    send_headers = {'Host':'	www.amazon.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept':'	text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive'}    
    
    
    req = request.Request(url,headers=send_headers)
    #with request.urlopen(req) as f:print('Status:', f.status, f.reason)
    f=request.urlopen(req)
    html=f.read().decode('utf-8')
    soup = BeautifulSoup(html,"html.parser")
    #print('Data:',html)
    fileName=str(uuid.uuid1())+'.txt'
    with open('C:/D/python/'+fileName, 'w',encoding='utf-8') as file:file.write(html)
    '''
    for tag in soup.find_all('span', class_='totalReviewCount'):
        print(tag.name)
        print(tag.contents)
    #print('go')
    ''' 
    i=1
    for div in soup.findChildren('div',class_='a-section review'):
        print(div['id'])
        print(i)
        i=i+1
        
    return html



#url='https://www.amazon.com/product-reviews/B00MQSMEEE/ref=cm_cr_arp_d_paging_btm_1?ie=UTF8&pageNumber=1&pageSize=50&sortBy=recent'
for i in range(1,10):
    starttime = datetime.datetime.now()
    getAmazonReviewPage('B00MQSMEEE',i)
    endtime = datetime.datetime.now()
    print (endtime - starttime)
   
#getAmazonReviewPage('B00MQSMEEE',2);


#import mysql.connector
