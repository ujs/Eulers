import numpy as np
N = np.ones((3,2))
b = np.arange(3)
c = b[:,np.newaxis]
# print(N)
# print (c)
# print(np.logaddexp(N,c))
#Array Centering
Y= np.random.random((10, 3))
Y_mean = Y.mean(0)
