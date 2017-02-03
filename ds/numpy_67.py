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
plt.ion
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()
plt.show()
import pandas as pandas

#precipitation data analysis
rainfall = pd.read_csv('precipitation.csv')['PRCP'].values
inches = rainfall / 254  # 1/10mm -> inches
inches.shape

