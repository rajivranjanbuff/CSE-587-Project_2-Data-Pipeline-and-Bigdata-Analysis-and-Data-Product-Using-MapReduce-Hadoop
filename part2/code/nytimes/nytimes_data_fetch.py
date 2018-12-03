#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:29:31 2018

@author: rajivranjan
"""
import time
import glob
from nytimesarticle import articleAPI
api = articleAPI('a13882b3917d46cb84dcd91efd77818c')

def parse_articles(articles):
  
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        news.append(dic)
    return(news) 


all_articles = []
for i in range(0,5):
    articles = api.search( q = 'trump',begin_date = 20180101,page=i )
    time.sleep(1)
    articles = parse_articles(articles)
    all_articles.append(articles)

current_working_dir = "/home/rajiv/hadoop/nytimes_input/"

import requests
from bs4 import BeautifulSoup
session = requests.Session()
for articles in all_articles:
    for news in articles:
        req = session.get(news['url'])
        soup = BeautifulSoup(req.text)
        paragraphs = soup.find_all('p', class_='story-body-text story-content')
        article=""
        for p in paragraphs:
            article = article + p.get_text()
            article_collec= current_working_dir  + str(time.time()) + '_article.txt'
            f = open(article_collec,'w')
            f.write(article)
            f.close()


read_files = glob.glob('/home/rajiv/hadoop/nytimes_input/*.txt')
with open("/home/rajiv/hadoop/nytimes_input/combined_article.txt","wb") as outfile:
    for f in read_files:
        with open(f,"rb") as infile:
            outfile.write(infile.read())
  
    

