import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def H(z,num,den):
	Num = np.polyval(num,pow(z,-1))
	Den = np.polyval(den,pow(z,-1))
	return Num/Den
	
x,fs = sf.read('Sound_Noise.wav')
order = 4
fc = 4000.0
Wn = 2*fc/fs
print ("Wn =",Wn)

# Filter Design
num, den = signal.butter(4, Wn, 'low', analog=False)
w = np.linspace(-np.pi,np.pi,len(x),endpoint=True)
H = H(np.exp(1j*w),num,den)

# Input in Frequency Domain
X = np.fft.fftshift(np.fft.fft(x))

# Output in Freqency Domain
Y = np.multiply(H,X)
y = np.fft.ifft(np.fft.ifftshift(Y)).real

sf.write('7.1_srikar.wav',y,fs)
output_signal = signal.filtfilt(num,den,x)


print(y)
print("\n")
print(output_signal)
print("\n")
print(H)

plt.figure(1)
plt.plot(y,'r')
plt.plot(output_signal,'g')
plt.figure(2)
plt.plot(y-output_signal)
plt.show()
