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
    personA = record[0]
    personB = record[1]

    print('%s\t%s' % (personA, personB))
    print('%s\t%s' % (personB, personA))