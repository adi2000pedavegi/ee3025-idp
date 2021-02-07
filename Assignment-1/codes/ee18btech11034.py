#Code by P.Aditya
#7th Febrauary 2021

import soundfile as sf
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

#Defining H(z) from numerator and denominator coefficents
def H(z,num,den):
	Num = np.polyval(num,z**(-1))
	Den = np.polyval(den,z**(-1))
	return Num/Den

#Reading the soundfile 	
x,fs = sf.read('Sound_Noise.wav')
order = 4
fc = 4000.0
Wn = 2*fc/fs

#Passing butterworth filter
num,den = signal.butter(order,Wn,'low')

#Preparing own routine filter design
#Constructing H(z)
k = np.arange(len(x))
w = 2*np.pi*k/len(x)
z = np.exp(1j * w)
H_z = H(z,num,den)

#Computing DFT(FFT) of x(n)
X = np.fft.fft(x)

#Multiplying X and H to give Y and computing IDFT(IFFT) to give y(n)
Y = np.multiply(H_z,X)
y = np.fft.ifft(Y).real

#Writing the sound file 
sf.write('7.1_Sound_With_ReducedNoise.wav',y,fs)

#Obtaining y(n) using builtin signal.filifilt
output_signal = signal.filtfilt(num,den,x)

#Plotting

plt.figure(figsize=(8,7))
plt.subplot(2,1,1)
plt.plot(y,'g')
plt.title('Output with own routine')
plt.grid()

plt.subplot(2,1,2)
plt.plot(output_signal,'r')
plt.title('Output with built in command')
plt.grid()
#plt.show()

plt.savefig('../figs/ee18btech11034.eps')
#If using termux
#subprocess.run(shlex.split("termux-open ../figs/Plot.pdf"))
