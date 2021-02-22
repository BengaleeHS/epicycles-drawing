import numpy as np 
import matplotlib.pyplot as plt
twopi = np.pi *2

def ndft(signal):
    C = []
    for i in range(len(signal)):
        C.append(dft(signal[i]))
    return C

def dft(signal):
    R = []
    N = len(signal)
    for k in range(N):
        c = 0
        for n in range(N):
            c= c+signal[n] * np.exp(-twopi * n * k * 1J/N)
        R.append(c)
    return R

def coef(signal):
    N=len(signal)
    M = N//2+1
    coef = np.array(ndft(signal))[:,:M]
    an = coef.real/N*2
    an[0]/=2
    bn = -coef.imag/N*2
    return an,bn
'''
x = [1,2,3,2,1,2]
N=len(x)
M = (N+1)//2
coef = np.array(ndft([x]))[0]
an = coef.real/N*2
an[0]/=2
bn = -coef.imag/N*2
k = np.fft.rfftfreq(N)
print(an)
def calc(t):
    c = 0
    for i in range(0,M):
        c+=(an[i]*np.cos(twopi*k[i]*N*t/100)+bn[i]*np.sin(twopi*k[i]*N*t/100))
    if N%2==0:
        c+= an[M]*np.cos(twopi*k[M]*N*t/100)/2
    return c

t = np.arange(0,100,100/N)
a = np.array([calc(i) for i in t])
fig = plt.figure()
ax = plt.axes()
plt.plot(t,a)
plt.plot(np.arange(0,100,100/N),x,'ro')
plt.show()
'''