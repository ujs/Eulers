import json
#path = open('sample.txt', "r", encoding='utf-8')
path = open('sample.txt')
records = [json.loads(line) for line in path]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]




##def tz_counts(sequence):
##    count = {}
##    for i in sequence:
##        if i in count:
##            count[i] += 1
##        else:
##            count[i] = 1
##
##    return count

##count_dict = tz_counts(time_zones)
##
##def top_counts(count_dict,n=10):
##    value_key_pair = [(count,tz) for tz, count in count_dict.items()]
##    value_key_pair.sort()
##    return value_key_pair[-n:]

##from collections import Counter
##
##counter = Counter(time_zones)
##counts.most_common(10)

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
frame = DataFrame(records)

tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('Missing')

clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()

results = Series([x.split()[0] for x in frame.a.dropna()])

cframe = frame[frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')


