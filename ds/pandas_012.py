#Series
import numpy as np 
import pandas as pd 

data = pd.Series([1,4,6,3,2], index = ['a','b','c','d','e'])
# print(data['c'])


pop_dict = {'Cal': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(pop_dict)

data_strange = pd.Series({2:'a',1:'b',3:'c'}, index = [3,4])
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
states = pd.DataFrame({'population': population,
                       'area': area})

#Data Frame Construction

#1
pd.DataFrame (population, columns = ['population'])
#2
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])

# df dict 
area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})

print(data['pop'])
print(data['area'])