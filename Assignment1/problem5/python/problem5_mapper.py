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
    id = record[0]
    sequence = record[1]
    sequence = sequence[:-10]

    print('%s\t%s' % (sequence, id))