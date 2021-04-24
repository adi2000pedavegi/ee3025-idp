#THIS PROGRAM GENERATES THE CHEBYSCHEV POLYNOMIAL COEFFICIENTS OF ORDER N
def cheb(N):
	import numpy as np
	v = np.array([1,0])
	v = v.flatten()
	u = np.array([1])
	u = u.flatten()
	if N == 0 :
		w = u
	elif N == 1 :
		w = v
	else :
		for i in range(N-1):
			temp = np.array([2,0])
			temp = temp.flatten()
			p = np.convolve(temp,v)
			m = len(p)
			n = len(u)
			
			w = p + np.hstack((np.zeros((1,m-n)).ravel(),u))
			
			u = v 
			v = w
	
	return w
#print("\n") 
			
