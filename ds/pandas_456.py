import numpy as np
import pandas as pd

# cali = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
# cali.isnull()
# cali.isnull().sum()
# cali

index = [('California', 2000), ('California', 2010), ('Texas', 2000), ('Texas', 2010)]
popu = [31000000, 32000000, 20000000, 21000000]
# population = pd.Series(popu, index = index)
# index1 = pd.MultiIndex.from_tuples(index)
# population = population.reindex(index1)
# population_df = population.unstack()

# pop_2 = pd.DataFrame(popu, index = [['Cal','Texas'],[2000,2010]], columns = ['population'])
data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}