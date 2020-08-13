#!/usr/bin/env python

import sys
import json

# sys.stdin = open('D:/_Study/BigData/Assignment1/MapReduce+Assignments_data_/MapReduce_Assignments/problem4/middle.txt', 'r')

# maps words to their counts
sequences = []

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    sequence, id = line.split('\t', 1)
    try:
        if sequence not in sequences:
            sequences.append(sequence)
    except ValueError:
        pass

jenc = json.JSONEncoder()
# write the results to STDOUT (standard output)
for sequence in sequences:
    print(jenc.encode(sequence))
 
