
import pandas as pd 
from pandas_datareader import data 
import matplotlib.pyplot as plt 
import seaborn; seaborn.set()

# goog = data.DataReader('GOOG', start = 2010, end = 2017, data_source = 'google' )
# goog.plot(alpha=0.5, style='-')
# goog.resample('BA').mean().plot(style=':')
# goog.asfreq('BA').plot(style='--');
# plt.legend(['input', 'resample', 'asfreq'], loc='upper left')

bike_data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
bike_data_W = bike_data['Fremont Bridge West Sidewalk']
bike_data_E = bike_data['Fremont Bridge East Sidewalk']

weekly = data.resample('W').sum()
# weekly.plot(style=[':', '--', '-'])
# plt.ylabel('Weekly bicycle count')