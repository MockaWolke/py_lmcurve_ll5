"""Plots a single fit using numpy and matplotlib"""
from py_lmcurve_ll5 import LL5Params, lmcurve_ll5, fix_ll5
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,]
y = [10,9.5,9,8,5,2,1,0]


params : LL5Params = lmcurve_ll5([float(i) for i in x],[float(i) for i in y], d=y[0])
func = fix_ll5(params=params)

x_axis = np.linspace(x[0], x[-1], 50)


plt.scatter(x,y)
plt.plot(x_axis, func(x_axis))
plt.show()
