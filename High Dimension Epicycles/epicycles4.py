import numpy as np 
import matplotlib.pyplot as plt  
from matplotlib import animation,rc
from mpl_toolkits.mplot3d import Axes3D
import ndft
twopi = np.math.pi*2
x = [2, 3, 1, 5, 6, 13, 34]
y = [7, 4, 3, 6, 4, 23, 64]
z = [1,2,3,4,1,2,3]
t = np.linspace(0,twopi,100)
x = np.sin(t).tolist()
y = np.cos(t).tolist()
z = np.sin(5*t).tolist()
w = np.cos(5*t).tolist()
N = len(x)
data = [x,y,z,w]
M = (N+1)//2
coef = np.array(ndft.ndft(data))
an = coef.real/N*2
an[:,0] /=2
bn = coef.imag/N*2 
an = an.T
bn=bn.T

trail =np.array([x[0],y[0],z[0],w[0]])
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax2.set_xlabel('Z')
ax2.set_ylabel('W')
ax.scatter(x,y,s=10)
ax2.scatter(z,w,s=10)
finalvec1, = ax.plot([0],[0],'ro')
finalvec2, = ax2.plot([0],[0],'ro')
#lines, = ax.plot3D([],[],[])

def animate(t):
    global trail
    vec = np.array([0.,0.,0.,0.])
    for k in range(M):
        
        a = np.array(an[k])
        b = np.array(bn[k])
        if(np.linalg.norm(a)!=0):
            x = a / np.linalg.norm(a)
            y = b - np.dot(x,b)*x
            if(np.linalg.norm(y)!=0):
                y = y / np.linalg.norm(y)
        elif(np.linalg.norm(b)!=0):
            y =  b / np.linalg.norm(b)
            x = a - np.dot(y,a)*y
            if(np.linalg.norm(x)!=0):
                x = x / np.linalg.norm(x)
        else:
            continue
        ax = np.dot(a,x)
        bx = np.dot(b,x)
        ay = np.dot(a,y)
        by = np.dot(b,y)
        theta = np.math.atan2(ay-bx,ax+by)
        phi = np.math.atan2(ay+bx,ax-by)
        A = 0.5*np.math.sqrt((ax+by)**2+(ay-bx)**2)
        B = 0.5*np.math.sqrt((ax-by)**2+(ay+bx)**2)
        vec+=np.array(A*(x*np.math.cos(k*twopi/N*t+theta)+y*np.math.sin(k*twopi/N*t+theta))+B*(x*np.math.cos(-k*twopi/N*t+phi)+y*np.math.sin(-k*twopi/N*t+phi)))
    if(N%2==0):
        a = np.array(an[M])
        b = np.array(bn[M])
        if(np.linalg.norm(a)!=0):
            x = a / np.linalg.norm(a)
            y = b - np.dot(x,b)*x
            if(np.linalg.norm(y)!=0):
                y = y / np.linalg.norm(y)
        elif(np.linalg.norm(b)!=0):
            y =  b / np.linalg.norm(b)
            x = a - np.dot(y,a)*y
            if(np.linalg.norm(x)!=0):
                x = x / np.linalg.norm(x)
        ax = np.dot(a,x)
        bx = np.dot(b,x)
        ay = np.dot(a,y)
        by = np.dot(b,y)
        theta = np.math.atan2(ay-bx,ax+by)
        A = 0.5*np.math.sqrt((ax+by)**2+(ay-bx)**2)
        vec+=np.array(A*(x*np.math.cos(M*twopi/N*t+theta)+y*np.math.sin(M*twopi/N*t+theta)))
    trail = np.vstack((trail,vec))
    finalvec1.set_data(vec[0],vec[1])
    finalvec2.set_data(vec[2],vec[3])

anim = animation.FuncAnimation(fig, animate , frames=np.linspace(0,N,100), interval=20, blit=False, repeat=True)
plt.show()