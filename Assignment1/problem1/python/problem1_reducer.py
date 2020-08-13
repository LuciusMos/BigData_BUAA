#!/usr/bin/env python

import sys
import json
 
# maps words to their counts
word2fileNames = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, fileName = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        word2fileNames.setdefault(word, [])
        if fileName not in word2fileNames[word]:
            word2fileNames.get(word, []).append(fileName)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        pass

# write the results to STDOUT (standard output)
jenc = json.JSONEncoder()
for word in word2fileNames:
    temp = (word, word2fileNames[word])
    print(jenc.encode(temp)) 
 
