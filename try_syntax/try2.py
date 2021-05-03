import numpy as np
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end if



n = np.arange(10)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))

hn = hn1 + hn2

H = np.fft.fft(hn)

print(hn)
print("\n")
print(H)
