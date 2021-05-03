#Code by P.Aditya
#21st March 2021

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

#padding zeros to original signal to make is length as 2**n
N_original = len(x)
temp = int(np.log2(N_original)) +1
N_fft = 2**temp
x_fft = np.pad(x, (0,N_fft-N_original), 'constant', constant_values=(0))
temp1 = np.fft.fft(x_fft)

#Passing butterworth filter
num,den = signal.butter(order,Wn,'low')

#Preparing own routine filter design
#Constructing H(z)
k = np.arange(len(x_fft))
w = 2*np.pi*k/len(x_fft)
z = np.exp(1j * w)
H_z = H(z,num,den)

temp2 = np.multiply(H_z,temp1)
temp3 = np.fft.ifft(temp2).real


sf.write('7.1_Sound_With_ReducedNoise.wav',temp3,fs)

