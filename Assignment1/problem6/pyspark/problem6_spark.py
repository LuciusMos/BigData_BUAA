from pyspark import SparkContext
import json

inputPath = "file:///Assignment1/problem6/matrix.json"
outputPath = "file:///Assignment1/problem6/output_spark"

def flatMapper(line):
    line = line.strip()
    record = json.loads(line)
    maxI = 10
    maxJ = 10
    results = []
    if record[0] == 'a':
        i = record[1]
        for j in range(maxJ + 1):
            results.append(((i, j), record))
    elif record[0] == 'b':
        j = record[2]
        for i in range(maxI + 1):
            results.append(((i, j), record))
    return(results)

def mapper(line):
    pos = line[0]
    abs = line[1]
    a_rows = list(filter(lambda x : x[0] == 'a', abs))
    b_rows = list(filter(lambda x : x[0] == 'b', abs))
    result = 0
    for a in a_rows:
        for b in b_rows:
            if a[2] == b[1]:
                result += a[3] * b[3]
    return((pos, result))

sc = SparkContext('local', 'test')
textFile = sc.textFile(inputPath)
multiply = textFile.flatMap(flatMapper).groupByKey().map(mapper).filter(lambda x : x[1]!=0).map(lambda x : json.dumps(x))
# multiply.foreach(print)
multiply.saveAsTextFile(outputPath)