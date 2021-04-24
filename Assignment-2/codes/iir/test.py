import numpy as np
from lattice import *

c = np.loadtxt('dignum.dat')
v = np.loadtxt('digden.dat')

temp = []
for i in range(len(v)):
	
	temp.append(v[i])

v = temp
u = v[::-1]
m = len(v)
K = np.zeros((1,m)).T
K[m-2] = v[m-1]
C = np.zeros((1,m)).T
C[m-1] = c[m-1]

while (m>1 and K[m-2] != 1):
		c = c - (C[m-1])*u
		v = (v - (K[m-2])*u)/(1 - K[m-2]**2)
		m = m-1
		v = v[0:m]
		c = c[0:m]
		
		u = v[::-1]
		if m > 1:
			K[m-2] = v[m-1]
		C[m-1] = c[m-1]

#print("c",c)
#print("C",C)
#print("K",K)
#print("m",m)
#print("u",u)
#print("v",v)
