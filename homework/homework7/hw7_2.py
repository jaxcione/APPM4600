import numpy as np 
import matplotlib.pyplot as plt 
import math

def f(x):
    return (1 + (10*x) ** 2) **(-1)

def phi(x,N,xi):
    z=1
    for k in range(N):
        z*=(x-xi[k])
    return z

def w_j(xj,xi,N):
    wj=1
    for n in range(N):

        if xj==xi[n]:
            continue
        else:
            wj*=1/(xj-xi[n])
    return wj

def P(x,N):
    x0=[]
    for i in range(1,N+1):
        x0.append(-1+(2*(i-1))/(N-1)) #x0 vector
    x0=np.array(x0) 
    p=0
    for s in range(N):
        p+=w_j(x0[s],x0,N)*f(x0[s])/(x-x0[s])
    return phi(x,N,x0)*p

X=np.linspace(-1,1,1001)
N=[5,10,15,20,25]
#[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
colors=['blue','orange','green','red','purple','brown','pink','gray','olive','cyan','brown','blueviolet',
        'darkorange','darkgreen','darkred','darkblue','darkcyan','darkmagenta','gold','lightcoral']
for M in N:
    plt.plot(X,P(X,M),label=f"Lagrange interpolation, N={M}",color=colors[M-18],marker='o',linestyle='solid',markersize=1)
    plt.plot(X,f(X),label='Actual function',color='k',linestyle='dotted')
    plt.ylim(0,1.2)
    plt.xlim(-1,1)
    plt.legend()
    plt.show()


