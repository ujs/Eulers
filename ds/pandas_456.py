import numpy as np
import pandas as pd

# cali = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
# cali.isnull()
# cali.isnull().sum()
# cali

index = pd.MultiIndex.from_arrays([['CA','CA','TX','TX'],[2000,2010,2000,2010]])
data = pd.DataFrame([1,2,3,4], index = index, columns = ['fig'])
data.index.names = ['state','year']
# print(data)

#Multiindex for both rows and columns
index = pd.MultiIndex.from_tuples([('city1',2000),('city1',2010),('city2',2000),('city2',2010)])
column =pd.MultiIndex.from_tuples([('car1',2000),('car1',2010),('car2',2000),('car2',2010)])
# values = np.random.randn(4,4)
# df = pd.DataFrame(values, index = index, columns = column)