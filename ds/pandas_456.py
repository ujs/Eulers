import numpy as np
import pandas as pd

# cali = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
# cali.isnull()
# cali.isnull().sum()
# cali

index = pd.MultiIndex.from_array([['CA','TX'],[2000,2010]])
data = pd.DataFrame([1,2,3,4], index = index, column = 'fig')
print(data)