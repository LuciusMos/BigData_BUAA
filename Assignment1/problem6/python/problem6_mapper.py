import sys
import json

# sys.stdin = open('D:/_Study/BigData/Assignment1/MapReduce+Assignments_data_/MapReduce_Assignments/problem6/matrix.json', 'r')
# sys.stdout = open('D:/_Study/BigData/Assignment1/MapReduce+Assignments_data_/MapReduce_Assignments/problem6/middle.txt', 'w')

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the line with json method
    record = json.loads(line)

    maxI = 10
    maxJ = 10
    if record[0] == 'a':
        i = record[1]
        for j in range(maxJ + 1):
            pos = (i, j)
            print('%s\t%s' % (json.dumps(pos), json.dumps(record)))
    elif record[0] == 'b':
        j = record[2]
        for i in range(maxI + 1):
            pos = (i, j)
            print('%s\t%s' % (json.dumps(pos), json.dumps(record)))