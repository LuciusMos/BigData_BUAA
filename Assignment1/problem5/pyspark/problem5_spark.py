from pyspark import SparkContext
import json
import sys

inputPath = "file:///Assignment1/problem5/dna.json"
outputPath = "file:///Assignment1/problem5/output_spark"
# sys.stdout = "d:/_Study/BigData/Assignment1/MapReduce_Assignments/problem5/anoutput.txt"

def mapper(line):
    line = line.strip()
    record = json.loads(line)
    id = record[0]
    sequence = record[1]
    sequence = sequence[:-10]
    return((sequence, id))

sc = SparkContext('local', 'test')
textFile = sc.textFile(inputPath)
unique_trim = textFile.map(mapper).groupByKey().map(lambda x : json.dumps(x[0]))
# unique_trim.foreach(print)
unique_trim.saveAsTextFile(outputPath)