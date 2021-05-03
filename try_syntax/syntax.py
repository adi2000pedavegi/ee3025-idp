#import numpy as np
#import matplotlib.pyplot as plt
#import math 
#import cmath 

#from add import *
#from bilin import *
#from cheb import *
#from lattice import *
#from lp_stable_cheb import *
#from lpbp import *
#from polypower import *

#x = np.linspace(-2,2,100)
#plt.plot(x,np.sin(x),x,np.cos(x))
#plt.legend(["blue", "green"], loc ="lower right")
#plt.show()
#print(cmath.acosh(0.99)**2)
#print(1/np.sqrt(1 + 0.6**2*np.cosh(4*cmath.acosh(0))**2).real)

#k = -20*np.log10(0.15)
#print(k)

#v = np.array([1])
#v = v.flatten()
#print(len(v))

#c = np.array([2,0])
#c = c.flatten()
#print(c)

#k = np.convolve(c,v)
#print(k)

#f = np.hstack((np.zeros((1,2)).ravel(),1))
#print(f)

#k = polypower([1,1],2)
#print(k)

#import numpy as np

#def lpbp(p,Omega0,B,Omega_p2):
	#import numpy as np
	#This function transforms the lowpass stable filter obtained
    #from the Chebyschev approximation to the bandpass
    #equivalent
    #[num,den,G] = lpbp(p,Omega0,B,Omega_p2)
    #Omega0 and B are the lowpass-bandpass transformation parameters
    #and Omega_p2 is the lower limit of the passband, used
    #to evaluate the gain G_bp
    #H(s) = G/p(s) is the stable low pass Cheybyschev approximation
    #Hbp(s) = G_bp*num(s)/den(s) is the corresponding bandpass stable
    #filter
     
	#N = len(p)
	#const = np.array([1,0,Omega0**2])
	#const = const.flatten()
	#v = const
	#v = np.array([1,0,Omega0**2])
	#v = v.flatten()
	#if N > 2:
		#for i in range(0,N-1):
			#M = len(v)
			#v[M-i-2] = v[M-i-2] + p[i+1]*(B**(i+1))
			#print(const)
			#print(v)
			#if i < N-2:
				#v = np.convolve(const,v)
			#print(v)
			#print(len(v))
		#den = v
		
	#elif N == 2:
		#M = len(v)
		#v[M-2] = v[M-2] + p[N-1]*B
		#den = v
	#else :
		#den = p
	
	#num = np.hstack((1,np.zeros((1,N-1)).ravel()))
	#G_bp = abs(np.polyval(den,1j*Omega_p2)/(np.polyval(num,1j*Omega_p2)))
	#return num,den,G_bp

#print("\n")

#p = np.array([1,1.10677989463470,1.61248086758380,0.914021007710573,0.336572800445907])
#p = p.flatten()
#B = 0.0953
#Omega_0 = 0.4594
#Omega_p1 = 0.9425
		
#[a,b,c] = lpbp(p,Omega_0,B,Omega_p1)		
#print(p[1]*B)


