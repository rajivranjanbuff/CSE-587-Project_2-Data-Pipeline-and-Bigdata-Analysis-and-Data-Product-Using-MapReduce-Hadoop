# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 02:11:41 2018

@author: rajiv
"""
import glob
import sys

read_files = glob.glob('/home/rajiv/hadoop/twitter_input/*.txt')
with open("/home/rajiv/hadoop/twitter_input/comb.txt","wb") as outfile:
    for f in read_files:
        with open(f,"rb") as infile:
            outfile.write(infile.read())
            




fh = open("/home/rajiv/hadoop/twitter_input/comb.txt", "r")
lines = fh.readlines()
fh.close()
    
# Weed out blank lines with filter
lines = filter(lambda x: not x.isspace(), lines)
    
# Write
fh = open("/home/rajiv/hadoop/twitter_input/combined_tweet.txt", "w")
fh.write("".join(lines))

    # should also work instead of joining the list:
    # fh.writelines(lines)
fh.close()