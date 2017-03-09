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
