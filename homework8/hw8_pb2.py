import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+(x)**2)


def l_i(x,z,i):
    num,denom=1,1
    n=len(z)#length of vector

    for s in range(n):
        if i==s:
            continue
        else:
            num*=(x-z[s])
            denom*=(z[i]-z[s])
    return num/denom

def pol_lagrange(z,x,n):
    m=0
    for k in range(n):
        m+=f(z[k])*l_i(x,z,k)
    return m


N=[5,10,15,20]
interval=np.linspace(-5,5,1000)


for j in range(len(N)):
    plt.figure()
    x_vals=np.linspace(-5,5,N[j])
    y_interp=np.array([pol_lagrange(x_vals, xi, N[j]) for xi in interval])
    
    plt.plot(interval,f(interval),'k--',label="f(x)")
    plt.plot(interval,y_interp,label=f"Lagrange interpolation N={N[j]}")
    plt.legend(loc='upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    

plt.show()