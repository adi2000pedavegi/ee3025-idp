import numpy as np
import soundfile as sf

x = np.array([1,2,3,4,4,3,2,1])
print(np.fft.fft(x))
x = np.array(x).reshape(len(x),1)
def fft(x):
	N = len(x)
	if(N==2):
		return np.vstack((x[0]+x[1],x[0]-x[1]))
	
	else:
		Xeven = fft(x[0::2])
		Xodd  = fft(x[1::2])
		
		dummy = np.ogrid[:int(N/2)]
		Wnu = np.exp(-1j*2*np.pi*dummy/N)
		Wnu = np.array(Wnu).reshape(len(Xodd),1)
		
		X = np.vstack((Xeven + np.multiply(Wnu,Xodd),Xeven - np.multiply(Wnu,Xodd)))
		
	return X



num = [1,0,1]
den = [0.5,1]

def H(z,num,den):
	Num = np.polyval(num,z**(-1))
	Den = np.polyval(den,z**(-1))
	return Num/Den

k = np.arange(len(x))
w = 2*np.pi*k/len(x)
z = np.exp(1j * w)
H_z = H(z,num,den)
print(fft(x))
print(np.array(H_z).reshape(len(x),1))
Y = np.multiply(np.array(H_z).reshape(len(x),1),fft(x))
print(Y)
print("**************************************************************************")

def ifft(Y):
	N = len(Y)
	if(N==2):
		return np.vstack(((Y[0]+Y[1])/2,(Y[0]-Y[1])/2))
	
	else:
		Yeven = ifft(Y[0::2])
		Yodd  = ifft(Y[1::2])
		
		dummy = np.ogrid[:int(N/2)]
		Wnu = np.exp(1j*2*np.pi*dummy/N)
		Wnu = np.array(Wnu).reshape(len(Yodd),1)
		Y1 = (Yeven + np.multiply(Wnu,Yodd))/2
		Y2 = (Yeven - np.multiply(Wnu,Yodd))/2
		y = np.vstack((Y1,Y2))
		y = y.real
		
	return y
y = ifft(Y)
y = y.flatten()
print(y)
Ydash = np.array([26.66666667+ 0.j , -6.3174688 + 0.87226042j , 0.+0.j , 0.67040998-0.53950429j , 0.+0.j , 0.67040998+0.53950429j , 0.-0.j , -6.3174688 -0.87226042j])
print(Ydash)
print(np.fft.ifft(Ydash))

