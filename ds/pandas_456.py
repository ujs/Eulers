import numpy as np
import pandas as pd

# cali = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
# cali.isnull()
# cali.isnull().sum()
# cali

index = pd.MultiIndex.from_arrays([['CA','CA','TX','TX'],[2000,2010,2000,2010]])
data = pd.DataFrame(np.random.rand(4,1), index = index, columns = ['fig'])
print(data)