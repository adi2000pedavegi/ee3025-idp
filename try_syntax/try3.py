import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if


k = 12
h = np.zeros(k)
h[0] = 1
h[1] = -0.5*h[0]
h[2] = -0.5*h[1] + 1

for n in range(3,k-1):
		h[n] = -0.5*h[n-1]

H = np.fft.fft(h)

print(h) 
print("\n")
print(H)
