import numpy as np
import pandas as pd

# cali = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
# cali.isnull()
# cali.isnull().sum()
# cali

index = [('California', 2000), ('California', 2010), ('Texas', 2000), ('Texas', 2010)]
popu = [31000000, 32000000, 20000000, 21000000]
population = pd.Series(popu, index = index)
index = pd.MultiIndex.from_tuples(index)
population.reindex(index)
print(index)
# print(population['California'])
print(population[2000])
