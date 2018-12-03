#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 00:00:52 2018

@author: rajivranjan
"""

#import all the necessary packages
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import time

# consumer key, consumer secret, access token, access secret.
consumer_key = 'FEkVk9lXsNbEJgrXSY7R2jx7j'
consumer_secret = '6fydOHWPKHToYOCtxtkNwIq6BIooIEB9xcZ5azWIQZg2wx5K0x'
access_token = '960957382426808320-PGjSooImBn0Sc6YJhR2bpfHjy7kSvAj'
access_secret = 'R5YrZFaYvikCZyBw06TlUgR7AeBb8K5yF24fpho4ZDpUR'

#no of tweets
MAX_TWEETS = 2000

#setting the auth path 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
#collecting tweets
api = API(auth, wait_on_rate_limit=True)
data = Cursor(api.search, q='#president').items(MAX_TWEETS)
#trump,trumptower,president,donaltrump
#collecting data
easter_data = []

current_working_dir = "./twitter_input/"
log_tweets = current_working_dir  + str(time.time()) + '_trump.txt'
with open(log_tweets, 'w') as outfile:
    for tweet in data:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            outfile.write(str(tweet.text))
            outfile.write("\n")