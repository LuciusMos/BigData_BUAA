from pyspark import SparkContext
import json

inputPath = "file:///Assignment1/problem4/friends.json"
outputPath = "file:///Assignment1/problem4/output_spark"

def flatMapper(line):
    line = line.strip()
    record = json.loads(line)
    personA = record[0]
    personB = record[1]
    results = []
    results.append(((personA, personB), 1))
    results.append(((personB, personA), 1))
    return results

sc = SparkContext('local', 'test')
textFile = sc.textFile(inputPath)
asym_friendship = textFile.flatMap(flatMapper).reduceByKey(lambda a, b : a+b).filter(lambda x : x[1]==1).map(lambda x : json.dumps(x[0]))
# asym_friendship.foreach(print)
asym_friendship.saveAsTextFile(outputPath)