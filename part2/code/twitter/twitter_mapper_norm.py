#!/usr/local/lib/python3.5/dist-packages
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

for line in sys.stdin:
    # remove leading and trailing whitespace
    
    line = line.strip()
    
    line = re.sub('[^a-zA-Z\n]',' ', line)
    line = re.sub(r'\b\w{1,3}\b','',line)
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(line) 
    bad_words = ['like','https','with','from','para','more','this','when','just','about','that','what','have','will','your']
    word_tokens = [w.lower() for w in word_tokens]
    word_tokens = [w.replace("qanon","QANON") for w in word_tokens]
    word_tokens = [w.replace("loquemasquiero","wishlist") for w in word_tokens]
    word_tokens = [w.replace("maga","MAGA") for w in word_tokens]
    word_tokens = [w.replace("potus","POTUS") for w in word_tokens]
    word_tokens = [w.replace("mexicanos","Mexicans") for w in word_tokens]
    word_tokens = [w.replace("mandar","Command") for w in word_tokens]
    word_tokens = [w.replace("unidos","UNIDOS") for w in word_tokens]
    word_tokens = [w.replace("sola","alone") for w in word_tokens]
    word_tokens = [w.replace("mensaje","message") for w in word_tokens]

#    for item in word_tokens:
#        item=item.lower()
    # split the line into words
   # words = line.split()
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = [w for w in word_tokens if not w in bad_words]
    #print(type(filtered_sentence))
#    for item in filtered_sentence:
#        item.lower()
    # increase counters
    for word in filtered_sentence:
        print('%s\t%s' % (word, "1"))
