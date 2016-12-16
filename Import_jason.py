
import json
path = open('sample.txt', "r", encoding='utf-8')
records = [json.loads(line) for line in path]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]




