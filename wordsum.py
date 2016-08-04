#!/usr/bin/python

import re
import string

def score(word):
    sanitised=(re.sub('[^a-zA-Z]','',word)).lower()
    total = 0
    for letter in sanitised:
	total += string.ascii_lowercase.index(letter)+1
    return total

words = open("/usr/share/dict/words", "r").readlines()

for w in words:
    print("{0} - {1}".format(score(w), w.rstrip()))
    #print((re.sub('[^a-zA-Z]','',w)).lower())
