import numpy as np
import matplotlib.pyplot as plt
import mpmath
import cmath

#THIS PROGRAM FINDS THE FIR COEFFICIENTS FOR A BANDPASS FILTER USING THE
#KAISER WINDOW AND THE DESIGN SPECIFICATIONS

#Filter number 
L = 114

#Sampling freqency (in kHz)
Fs = 48

#Constant used to get the normalized digital freqencies
const = 2*np.pi/Fs

#The permissible filter amplitude deviation from unity
delta = 0.15

#Bandpass filter specifications (kHz)

#Passband F_p2 < F_p1
F_p1 = 3 + 0.6*(L-107)
F_p2 = 3 + 0.6*(L-109)

#Transition band
delF = 0.3;

#Stopband F_s2 < F_p21; F_p1 < F_s1
F_s1 = F_p1 + 0.3
F_s2 = F_p2 - 0.3

#Normalized digital filter specifications (radians/sec)
omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_c = (omega_p1+omega_p2)/2
omega_l = (omega_p1-omega_p2)/2

omega_s1 = const*F_s1
omega_s2 = const*F_s2
delomega = 2*np.pi*delF/Fs

A = -20*np.log10(delta)
N = 100

n = np.linspace(-N,N,(2*N+1))
n = n.reshape((2*N+1),1)

hlp = np.sin(n*omega_l)/(n*np.pi)
hlp[N] = omega_l/np.pi
hbp = 2*hlp*np.cos(n*omega_c)

omega = np.linspace(-np.pi/2,np.pi/2,201)
z = np.exp(1j*omega)

Hlp = np.abs(np.polyval(hlp,z**(-1)))
plt.figure(1)
plt.plot(omega/np.pi,Hlp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{lp}(\omega)|$')
plt.grid()
plt.title("Lowpass FIR filter magnitude response")
plt.savefig('figs/ee18btech11034_FIR_Lowpass.eps')

Hbp = np.abs(np.polyval(hbp,z**(-1)))

fir_coeff = hbp
np.savetxt("fir_coeff.dat",fir_coeff)

plt.figure(2)
plt.plot(omega/np.pi,Hbp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{bp}(\omega)|$')
plt.grid()
plt.title("Bandpass FIR filter magnitude response")
plt.savefig('figs/ee18btech11034_FIR_Bandpass.eps')

#plt.show()


