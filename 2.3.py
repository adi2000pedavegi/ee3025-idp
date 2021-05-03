import soundfile as sf
from scipy import signal

#Read the .wav file
input_signal,fs = sf.read('Sound_Noise.wav')

#Sampling frequency of the input signal
sampl_freq = fs

#order of the filter 
order = 4

#cut -off frequency is set as 4kHz
cutoff_freq = 4000.0

#digital frequency
Wn = 2*cutoff_freq/sampl_freq

#b and a are numerator and denominator polynomials respectively
b,a = signal.butter(order,Wn,'low')

#filter the input signal with butterworth filter
output_signal = signal.filtfilt(b,a,input_signal)

#write the output signal into a .wav file
sf.write('Sound_With_ReducedNoise.wav',output_signal,fs)

print(input_signal)
print(output_signal)

print(len(input_signal))
print(len(output_signal))
