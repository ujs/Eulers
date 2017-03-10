from pandas_datareader import data 
import matplotlib.pyplot as pyplotimport seaborn; seaborn.set()

google = data.DataReader('GOOG', start = 2010, end = 2017, data_source = 'google' )