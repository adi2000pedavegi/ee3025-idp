import numpy as np

def add(x,y):
	#This fuctions adds two polynomials defined by vectors x and y 
    #z = add(x,y)
    
	import numpy as np
	m = len(x)
	n = len(y)
	if (m == n):
		z = x + y
	elif m > n:
		z = x + np.hstack((np.zeros((1,m-n)).ravel(),y))
	else:
		z = np.hstack((np.zeros((1,n-m)).ravel(),x)) + y
	return z


#print("\n")

	
