#!/usr/bin/env python

import sys
import json

# sys.stdin = open('middle.txt', 'r')

# maps words to their counts
id2value = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    order_id, value = line.split('\t', 1)
    value = json.loads(value)
    try:
        id2value.setdefault(order_id, [])
        if value not in id2value[order_id]:
            id2value[order_id].append(value)
    except ValueError:
        pass

jenc = json.JSONEncoder()
# write the results to STDOUT (standard output)
for order_id in id2value:
    values = id2value[order_id]
    for value in values:
        if value[0] == 'order':
            order = value
            for value in values:
                if value[0] == 'line_item':
                    temp = (order + value)
                    print(jenc.encode(temp))
 
