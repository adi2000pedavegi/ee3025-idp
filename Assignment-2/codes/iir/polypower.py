
def polypower(v,N):
	import numpy as np
	y = np.array([1])
	y = y.flatten()
	if N > 0:
		for i in range(N):
			y = np.convolve(y,v)
	return y

#print("\n")
