from pyspark import SparkContext
import json

inputPath = "file:///Assignment1/problem1/books.json"
outputPath = "file:///Assignment1/problem1/output_spark"

def flatMapper(line):
    line = line.strip()
    record = json.loads(line)
    filename = record[0]
    temp = []
    temp.append(filename)
    filename = temp
    words = record[1].split(' ')
    results = []
    for word in words:
        results.append((word, filename))
    return results

def reducer(a, b):
    a = set(a)
    b = set(b)
    result = a.union(b)
    result = list(result)
    return(result)

sc = SparkContext('local', 'test')
textFile = sc.textFile(inputPath)
inverted_index = textFile.flatMap(flatMapper).reduceByKey(reducer).map(lambda x : json.dumps(x))
# inverted_index.foreach(print)
inverted_index.repartition(1).saveAsTextFile(outputPath)