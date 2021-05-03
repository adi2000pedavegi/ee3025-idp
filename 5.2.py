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
plt.stem(np.arange(12), hn1+hn2)
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()# minor
plt.show()

