import sys
import json

# sys.stdin = open('records.json', 'r')
# sys.stdout = open('middle.txt', 'w')

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the line with json method
    record = json.loads(line)
    name = record[0]

    print('%s\t%s' % (name, 1))