
import json


path = open('sample.txt', "r", encoding='utf-8')
record = [json.loads(line) for line in path]


print (len(record))
