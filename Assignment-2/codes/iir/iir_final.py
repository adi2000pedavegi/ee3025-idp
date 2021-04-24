import numpy as np
import matplotlib.pyplot as plt
from para import *
from lp_stable_cheb import *
from lpbp import *
from bilin import *

epsilon = 0.4
[p,G_lp] = lp_stable_cheb(epsilon,N)
Omega_L = np.linspace(-2,2,401)
H_analog_lp = G_lp*abs(1/np.polyval(p,1j*Omega_L))

plt.figure(1)
plt.plot(Omega_L,H_analog_lp);
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,LP}(j\Omega)|$')
plt.title('Analog Lowpass Chebyshev filter')
plt.savefig('figs/ee18btech11034_Analog_IIR_Lowpass.eps')

[num,den,G_bp] = lpbp(p,Omega_0,B,Omega_p1)

Omega = np.linspace(-0.65,0.65,131)
H_analog_bp = G_bp*abs(np.polyval(num,1j*Omega)/np.polyval(den,1j*Omega))

plt.figure(2)
plt.plot(Omega,H_analog_bp);
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,BP}(j\Omega)|$')
plt.title('Analog Bandpass Chebyshev filter')
plt.savefig('figs/ee18btech11034_Analog_IIR_Bandpass.eps')

[dignum,digden,G] = bilin(den,omega_p1)
omega = np.linspace(-2*np.pi/5,2*np.pi/5,801)

H_dig_bp = G*abs(np.polyval(dignum,np.exp(-1j*omega))/np.polyval(digden,np.exp(-1j*omega)))


iir_num = G*dignum
iir_den = digden

plt.figure(3)
plt.plot(omega/np.pi,H_dig_bp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{d,BP}(\omega)|$')
plt.title('Digital Bandpass Chebyshev filter')
plt.savefig('figs/ee18btech11034_Digital_IIR_Bandpass.eps')

np.savetxt("iir_num.dat",iir_num)
np.savetxt("iir_den.dat",iir_den)
np.savetxt("dignum.dat",dignum)
np.savetxt("digden.dat",digden)
np.savetxt("G.dat",np.array([G]))

#plt.show()

