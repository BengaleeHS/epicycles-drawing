import numpy as np 
import matplotlib.pyplot as plt  
from matplotlib import animation,rc
import cv2
import dft
def epicycle(x=None,y=None,precise=30):
    MAX_N = precise
    X = x
    Y = y

    points = X+Y*1j
    coeff = dft.dft(points)
    coeff.sort(key=lambda x: x['radius'],reverse = True)
    twopi = np.pi*2
    fig, ax = plt.subplots(figsize=(8,8))
    plt.axis('off')
    ax.set_xlim((-10,10))
    ax.set_ylim((-10,10))
    ax.set_ylim((-10,10))
    finalpoint, = plt.plot([0],[0],"bD",markersize=2)
    N = len(coeff)
    if N<MAX_N:
        MAX_N = N
    #make orbit equation
    for k in range(MAX_N):
        print(f"{coeff[k]['radius']:.3f} cos({N*coeff[k]['freq']:.0f}t{coeff[k]['phase']:+.3f}) + ", end='')
    print("i (",end='')
    for k in range(MAX_N):
        print(f"{coeff[k]['radius']:.3f} sin({N*coeff[k]['freq']:.0f}t{coeff[k]['phase']:+.3f})", end='')
        if k!=MAX_N-1:
            print(" + ",end='')
    print(')')
    #init orbits
    orbits = []
    connections = []
    offset = 0
    for i in range(MAX_N):
        t = np.arange(0,twopi,0.01)*1j
        s = offset+coeff[i]['c']*np.exp(t)
        connect, = plt.plot([offset.real,offset+coeff[i]['c'].real],[offset.imag,offset+coeff[i]['c'].imag],linewidth=1,color='red')
        offset += coeff[i]['c']
        orbit, = plt.plot(s.real,s.imag,linewidth=1,color='green')
        connections.append(connect)
        orbits.append(orbit)

    xdata,ydata = [],[]
    drawing, = plt.plot(xdata,ydata)

    def animate(i):
        offset = 0+0j
        for k in range(MAX_N):
            t = np.arange(0,twopi,0.01)*1j
            s = (offset+coeff[k]['c']*np.exp(t))
            orbits[k].set_data(s.real,s.imag)
            temp = offset
            offset+=coeff[k]['radius']*np.exp(1j*(N*coeff[k]['freq']*i+coeff[k]['phase']))
            connections[k].set_data([temp.real,offset.real],[temp.imag,offset.imag])
        finalpoint.set_data(offset.real,offset.imag)
        xdata.append(offset.real)
        ydata.append(offset.imag)
        drawing.set_data(xdata,ydata)

    anim = animation.FuncAnimation(fig, animate , frames=np.linspace(0,twopi,200), interval=10, blit=False, repeat=True)
    plt.show()
    np.random.seed(19680801)
    
    #anim.save('fourier drawing.mp4',writer='ffmpeg',fps=60,bitrate=2000,codec='h264')