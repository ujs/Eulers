from pandas_datareader import data 
import matplotlib.pyplot as pyplot
import seaborn; seaborn.set()

google = data.DataReader('GOOG', start = 2010, end = 2017, data_source = 'google' )
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'], loc='upper left')