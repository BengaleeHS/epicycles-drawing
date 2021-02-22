import numpy as np 
twopi = np.pi *2
def dft(signal):
    R = []
    N = len(signal)
    F = np.fft.fftfreq(N)
    for k in range(N):
        c = 0
        for n in range(N):
            c= c+signal[n] * np.exp(-twopi * n * F[k]*1J)
        c/=N
        R.append({'c':c, 'radius':np.math.sqrt(c.imag**2+c.real**2), 'phase':np.math.atan2(c.imag,c.real),'freq':F[k]})
    return R