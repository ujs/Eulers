import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,10,100)
y = np.sin(x)

#Contours
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plot.contourf(X,Y,Z,cmap='RdGy')