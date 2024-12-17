from py_lmcurve_ll5 import LL5Params, lmcurve_ll5

x = [1,2,3,4,5,6,7,8,]
y = [10,9.5,9,8,5,2,1,0]


a : LL5Params = lmcurve_ll5([float(i) for i in x],[float(i) for i in y])
print(a)
