import numpy as np
import pandas as pd

# cali = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
# cali.isnull()
# cali.isnull().sum()
# cali

index = [('California', 2000), ('California', 2010), ('Texas', 2000), ('Texas', 2010)]
popu = [31000000, 32000000, 20000000, 21000000]
# population = pd.Series(popu, index = index)
index = pd.MultiIndex.from_tuples(index)
pop_df.stack()
pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
pop_df


# pop[[i for i in pop.index if i[1] == 2010]]
# index = pd.MultiIndex.from_tuples(index)

pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
pop_df


