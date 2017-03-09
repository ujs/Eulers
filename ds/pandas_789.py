import pandas as pd 
import numpy as np 

def make_df(cols,ind):
	"""Make a df quick"""
	df = {c:[str(c)+str(i) for i in ind] for c in cols}
	return pd.DataFrame(df,ind)

class display(df_object):
	'''Good Display'''
	template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
    	self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_()) for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a)) for a in self.args)
    