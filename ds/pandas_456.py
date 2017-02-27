import numpy as np
import pandas as pd

cali = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
cali.isnull()
cali.isnull().sum()
cali

index = [('California', 2000), ('California', 2010), ('Texas', 2000), ('Texas', 2010)]