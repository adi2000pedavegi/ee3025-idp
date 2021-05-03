import numpy as np
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end if

#DTFT
def H(z):
	num = np.polyval([1,0,1],z**(-1))
	den = np.polyval([0.5,1],z**(-1))
	H = num/den
	return H
		


#Input and Output
k = np.arange(12)
omega = 2*np.pi*k/12
#omega = np.linspace(-np.pi,np.pi,12)


#subplots

print((H(np.exp(1j*omega))))
