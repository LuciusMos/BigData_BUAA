from pyspark import SparkContext
import json

inputPath = "file:///Assignment1/problem2/records.json"
outputPath = "file:///Assignment1/problem2/output_spark"

def mapper(line):
    line = line.strip()
    record = json.loads(line)
    order_id = record[1]
    return(order_id, record)

def flatMapper(line):
    values = line[1]
    result = []
    for value in values:
        if value[0] == 'order':
            order = value
            for value in values:
                if value[0] == 'line_item':
                    result.append(order + value)
    return(result)

sc = SparkContext('local', 'test')
textFile = sc.textFile(inputPath)
join = textFile.map(mapper).groupByKey().flatMap(flatMapper).map(lambda x : json.dumps(x))
# join.foreach(print)
join.saveAsTextFile(outputPath)