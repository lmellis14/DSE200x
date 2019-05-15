import pandas as pd
import numpy as np
import collections
from nltk.corpus import stopwords

file = open('C:/Users/Luke.Ellis/Documents/DataAnalytics/Data/98-0.txt','r', encoding='utf8')
file = file.read()

stopwords=stopwords.words('english')
wordcount = {}


for word in file.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
d=collections.Counter(wordcount)

for word,count in d.most_common(10):
    print(word," : " ,count)
