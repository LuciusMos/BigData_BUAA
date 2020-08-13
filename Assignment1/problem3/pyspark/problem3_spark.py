from pyspark import SparkContext
import json

inputPath = "file:///Assignment1/problem3/friends.json"
outputPath = "file:///Assignment1/problem3/output_spark"

sc = SparkContext('local', 'test')
textFile = sc.textFile(inputPath)
friend_count = textFile.map(lambda line : (json.loads(line)[0], 1)).reduceByKey(lambda a, b : a+b).map(lambda x : json.dumps(x))
# friend_count.foreach(print)
friend_count.saveAsTextFile(outputPath)