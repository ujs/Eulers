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

print("dimension of x3: ",x3.ndim)
print("shape of x3: ",x3.shape)
print("size of x3: ",x3.size)
print("bytesize of x3 item (in bytes): ",x3.itemsize)
print("total bytesize of x3 item (in bytes): ",x3.nbytes)
print (x3[0,1:3,:3])