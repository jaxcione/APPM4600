import numpy as np
import matplotlib.pyplot as plt
##################################################################################################
#Lagrange

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

##################################################################################################
#Hermite

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+(x)**2)

def f_prime(x):
    return -2*x/((1+(x**2))**2)


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

def l_i_prime(z,i):
    num,denom=1,1
    n=len(z)#length of vector
    sum=0
    for s in range(n):
            if i==s:
                continue
            else:
                num*=1
                denom=(z[i]-z[s])
                sum+=num/denom
    return sum


def Q(x,xj,i):
    return (1-2*(x-xj[i])*l_i_prime(xj,i))*(l_i(x,xj,i)*l_i(x,xj,i))

def R(x,xj,i):
    return (x-xj[i])*(l_i(x,xj,i)*l_i(x,xj,i))

def pol_hermite(z,x,n):
    p=0
    for k in range(n):
        p+=f(z[k])*Q(x,z,k)+f_prime(z[k])*R(x,z,k)
    return p



N=[5,10,15,20]
interval2=np.linspace(-5,5,1000)


for j in range(len(N)):
    plt.figure()
    t_vals=np.linspace(-5,5,N[j])
    y_interp=np.array([pol_hermite(t_vals, xi, N[j]) for xi in interval2])
    
    plt.plot(interval2,f(interval2),'k--',label="f(x)")
    plt.plot(interval2,y_interp,label=f"Hermite interpolation N={N[j]}")
    plt.legend(loc='upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    

plt.show()

