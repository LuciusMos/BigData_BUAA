#!/usr/bin/env python

import sys
import json

# sys.stdin = open('D:/_Study/BigData/Assignment1/MapReduce+Assignments_data_/MapReduce_Assignments/problem4/middle.txt', 'r')

# maps words to their counts
relate2count = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    personA, personB = line.split('\t', 1)
    relation = (personA, personB)
    relate2count.setdefault(relation, 0)
    try:
        relate2count[relation] += 1
    except ValueError:
        pass

asymFriends = filter(lambda x : relate2count[x] == 1, relate2count.keys())

jenc = json.JSONEncoder()
# write the results to STDOUT (standard output)
for asymFriend in asymFriends:
    print(jenc.encode(asymFriend))
 
