#!/usr/bin/env python

import sys
import json

# sys.stdin = open('middle.txt', 'r')

# maps words to their counts
name2count = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    name, count = line.split('\t', 1)
    try:
        count = int(count)
        name2count[name] = name2count.get(name, 0) + count
    except ValueError:
        pass

jenc = json.JSONEncoder()
# write the results to STDOUT (standard output)
for name in name2count:
    temp = (name, name2count[name])
    print(jenc.encode(temp))
 
