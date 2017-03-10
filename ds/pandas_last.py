from pandas_datareader import data 
import matplotlib.pyplot as plt 
import seaborn; seaborn.set()

goog = data.DataReader('GOOG', start = 2010, end = 2017, data_source = 'google' )
goog = goog['Close']
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'], loc='upper left')