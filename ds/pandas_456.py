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
values = np.random.randn(4,4)
df = pd.DataFrame(values, index = index, columns = column)

# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data

import pandas as pd 
import numpy as np 

def make_df(cols,ind):
	"""Make a df quick"""
	df = {c:[str(c)+str(i) for i in ind] for c in cols}
	return pd.DataFrame(df,ind)


   
## Concat
series1 = pd.Series(['x','y','z'], index = [1,2,3])
series2 = pd.Series(['a','b','c'], index = [4,5,6])
new_ser = pd.concat([series1,series2])

## Display
class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)
    



df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
display('df1', 'df2', 'pd.concat([df1, df2])')


