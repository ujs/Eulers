import pandas as pd 
import numpy as np 

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


df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
display('df1', 'df2')



df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux',
                               'spreadsheets', 'organization']})
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})

# US States Data Analysis

population = pd.read_csv("state-population.csv")
area = pd.read_csv("state-areas.csv")
abbrev = pd.read_csv("state-abbrevs.csv")
merged = pd.merge(population,abbrev,how='outer',left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation',1)


merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
final = pd.merge(merged,area,on = 'state',how ='right')

# Planets Data (Aggregations)
import seaborn as sns
# planets = sns.load_dataset('planets')

# decade = 10 * (planets['year'] // 10)
# decade = decade.astype(str) + 's'
# decade.name = 'decade'
# planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)