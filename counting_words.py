# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:24:31 2019

@author: Vlad
"""
from collections import Counter
with open('text.txt') as file:
        text = file.read()
text = text.replace("\n", " ")
text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
text = text.lower()
words = text.split()
words.sort()

words_count = Counter(words)
for word, count in words_count.most_common(10):
    print(word, count)
    
print('Всего слов:', len(words_count))
