
import json
path = open('sample.txt', "r", encoding='utf-8')
records = [json.loads(line) for line in path]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]




def tz_counts(sequence):
    count = {}
    for i in sequence:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count

count_dict = tz_counts(time_zones)

def top_counts(count_dict,n=10):
    value_key_pair = [(count,tz) for tz, count in count_dict.items()]
    value_key_pair.sort()
    return value_key_pair[-n:]

