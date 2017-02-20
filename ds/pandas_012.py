#Series
import numpy as np 
import pandas as pd 

data = pd.Series([1,4,6,3,2], index = [a,b,c,d,e])
# print(data['c'])


pop_dict = {'Cal': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(pop_dict)

data_strange = pd.Series({2:'a',1:'b',3:'c'}, index = [3,4])
