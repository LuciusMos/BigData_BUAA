#!/usr/bin/env python

import sys
import json

# sys.stdin = open('D:/_Study/BigData/Assignment1/MapReduce+Assignments_data_/MapReduce_Assignments/problem6/middle.txt', 'r')

# maps words to their counts
pos2ab = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    pos, ab = line.split('\t', 1)
    pos = tuple(json.loads(pos))
    ab = json.loads(ab)
    
    pos2ab.setdefault(pos, [])
    pos2ab[pos].append(ab)


jenc = json.JSONEncoder()
# write the results to STDOUT (standard output)
for pos in pos2ab.keys():
    abs = pos2ab[pos]
    a_rows = list(filter(lambda x : x[0] == 'a', abs))
    b_rows = list(filter(lambda x : x[0] == 'b', abs))
    result = 0
    for a in a_rows:
        for b in b_rows:
            if a[2] == b[1]:
                result += a[3] * b[3]
    if result != 0:
        temp = (pos, result)
        print(jenc.encode(temp))

 
