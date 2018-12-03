#!/usr/local/lib/python3.5/dist-packages
import sys
import csv
from collections import OrderedDict

from collections import Counter
import pandas as pd
word2count={}

for line in sys.stdin:
    line =line.strip()
    word,count=line.split('\t',1)
    
    try:
        count =int(count)
    except ValueError:
        continue
    
    try:
        word2count[word]=word2count[word]+count
    except:
        word2count[word]=count



top_ten=dict(Counter(word2count).most_common(20))
df = pd.DataFrame([[key,value] for key,value in top_ten.items()],columns=["name","count"])
df.to_csv('./twitter_output_norm/twitter_norm.csv',sep=',',encoding='utf-8',index=False)

print(top_ten)
