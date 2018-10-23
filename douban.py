#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 08:54:04 2018

@author: nuochen
"""

import urllib2   
import re   
from bs4 import BeautifulSoup  
import codecs  
import pandas as pd
import time


def crawl(url):  
    page = urllib2.urlopen(url)   
    contents = page.read()   
    soup = BeautifulSoup(contents, "html.parser")   
    
    #initialize dataframe 
    df = pd.DataFrame(columns = ['电影名称','评分','标签','评语','标记日期'])
  
    for tag in soup.find_all(attrs={"class":"item"}):  
        name = tag.find('em').get_text()
        d = {}
        d['电影名称'] = name
        
        rating5 = tag.find(attrs={"class":"rating5-t"})
        rating4 = tag.find(attrs={"class":"rating4-t"})
        rating3 = tag.find(attrs={"class":"rating3-t"})
        rating2 = tag.find(attrs={"class":"rating2-t"})
        rating1 = tag.find(attrs={"class":"rating1-t"})
        if rating5:
            d['评分'] = '5'
        elif rating4:
            d['评分'] = '4'
        elif rating3:
            d['评分'] = '3'
        elif rating2:
            d['评分'] = '2'
        elif rating1:
            d['评分'] = '1'
        else: 
            d['评分'] = 'None'
        
        tags = tag.find(attrs={"class":"tags"})
        if tags:
            d['标签'] = tags.get_text()
        else:
            d['标签'] = 'None'
            
        comment = tag.find(attrs={"class":"comment"})
        if comment:
            d['评语'] = comment.get_text()
        else:
            d['评语'] = 'None'
        
        date = tag.find(attrs={"class":"date"})
        d['日期'] = date.get_text()
        
        df = df.append(d, ignore_index = True)
            
    return df
  
 
if __name__ == '__main__':  
      
    #infofile = codecs.open("Result_Douban.txt", 'a', 'utf-8')       
    url = 'https://movie.douban.com/people/domitor/collect?start=0&sort=time&rating=all&filter=all&mode=grid'  
    i = 0  
    df = pd.DataFrame()
    while i < 95:  
        print u'页码', (i+1)  
        num = i*25 #每次显示25部 URL序号按25增加  
        url = 'https://movie.douban.com/people/domitor/collect?start=' + str(num) + '&sort=time&rating=all&filter=all&mode=grid'  
        new_df = crawl(url) 
        df = df.append(new_df)
        #infofile.write("\r\n\r\n\r\n")  
        i = i + 1  
        time.sleep(10)
    df.to_csv('douban_nuo_old.csv',encoding='utf8')