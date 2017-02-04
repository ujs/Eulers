import numpy as np
N = np.ones((3,2))
b = np.arange(3)
c = b[:,np.newaxis]
# print(N)
# print (c)
# print(np.logaddexp(N,c))
#Array Centering
Y = np.random.random((10, 3))
Y_mean = Y.mean(0)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
plt.ion
# plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
# plt.colorbar()
# plt.show()
import pandas as pd

#precipitation data analysis
rainfall = pd.read_csv('precipitation.csv')['PRCP'].values
inches = rainfall / 254  # 1/10mm -> inches
inches.shape
rainy = (inches>0)
days = np.arange(365)
summer = (days >170) & (days < 260)
print (np.median (inches[rainy]))


# plt.hist(inches,40);
# plt.show()
# print(np.sum((inches>0.5) & (inches<1)))
# print("Number days without rain:      ", np.sum(inches == 0))
# print("Number days with rain:         ", np.sum(inches != 0))
# print("Days with more than 0.5 inches:", np.sum(inches > 0.5))
      

#Boolean
a = np.array([2,4,3,7,4,8])
# print(a<4)
# print(a>4)
# print(a!=4)
# print((2*a)==(a**2))

# b = np.ones((2,6))
# print(b)

#RandomState
rng = np.random.RandomState(0)
b = rng.randint(10, size = (3,4))
# print(np.count_nonzero(a<10))
# print(np.sum(a>4))
# print(np.sum(a<6,axis=1))
# print(b<5)
# print (b[b>8])
A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
A | B




