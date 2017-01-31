import array
L = list(range(10))
A = array.array('i', L)
#print(A)

import numpy as np
np.array ([1,3,2,4,5])

#Numpy Array Attributes
np.random.seed(0)
x1 = np.random.randint(10, size = 6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

# print("dimension of x3: ",x3.ndim)
# print("shape of x3: ",x3.shape)
# print("size of x3: ",x3.size)
# print("bytesize of x3 item (in bytes): ",x3.itemsize)
# print("total bytesize of x3 item (in bytes): ",x3.nbytes)
x3_subarray = x3[0,1:3,:3].copy()
x3_subarray[1,1]= 200

x1_reshape = x1.reshape((2,3))

#Converting a given array into an array with reciprocals
np.random.seed(0)

def calculate_reci(values):
	output = np.empty(len(values))
	for i in range (len(values)):
		output[i] = 1.0/values[i]
	return output
values = np.random.randint(1,10,size=5)


#Vectorized Operations
#print (np.arange(5)/np.arange(1,6))


#Trig Functions
theta = np.linspace(0, np.pi, 3)
trig_sin = np.sin(theta)
trig_cos = np.cos(theta)
reverse_sin = np.arcsin(trig_sin)

x = np.array([0.001])
# print("exp(x)= ",np.exp(x), "exp(x)-1= ",np.expm1(x))

#Scipy
from scipy import special

a = np.random.randint(20)
# print (special.gamma(a))

L = np.random.random(100)
# print (sum(L))
# print (np.sum(L))
# print (L.sum())

# print (min(L),max(L))
# print (np.min(L))
M = np.random.random((3,4))
np.min(M)
np.sum(M)
print(M.min(axis = 0))
print(M.max(axis=1))

#President's age
import pandas as pd
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
# print (heights)
# print (heights.mean())
# print (heights.std())
# print (np.percentile(heights,25))




