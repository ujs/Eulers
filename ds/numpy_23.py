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

print(x3)
