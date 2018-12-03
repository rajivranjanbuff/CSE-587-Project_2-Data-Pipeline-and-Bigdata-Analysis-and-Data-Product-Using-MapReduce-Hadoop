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
    bad_words = ['last','been','week','their','will','over','other','when','were','than','about','first','with','have','after','what','more','they','year','said','there','which','from','this','that','former','general','would','year']
    word_tokens = [w.lower() for w in word_tokens]
    word_tokens = [w.replace("california","California") for w in word_tokens]
    word_tokens = [w.replace("trump","Trump") for w in word_tokens]
    word_tokens = [w.replace("government","Government") for w in word_tokens]
    word_tokens = [w.replace("department","Department") for w in word_tokens]
    word_tokens = [w.replace("mueller","Mueller") for w in word_tokens]
    

    
    # split the line into words
   # words = line.split()
    filtered_sentence = [w for w in word_tokens if not w in stop_words]  
    filtered_sentence = [w for w in word_tokens if not w in bad_words]
    
    # increase counters
    for word in filtered_sentence:
        print('%s\t%s' % (word, "1"))
