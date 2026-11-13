import numpy as np 
import matplotlib.pyplot as plt 
from scipy.special import gamma
import scipy.integrate as quad


def traps(a,b,n,f):
    t=np.linspace(a,b,n+1)
    z=f(t)
    h=(b-a)/n

    return (h/2)*(z[0]+2*np.sum(z[1:n])+z[-1])

def f_gamma(x,t):
    
    return t**(x-1)*np.exp(-t)


def f_prime2(x,t):                     
    return np.exp(-t)*t**(x -3)*((x-1)*(x-2)-2*(x-1)*t + t**2)

M=50
X=[2,4,6,8,10]
T=np.linspace(0.000001,M,10000)
eps=1E-3
K=max(abs(f_prime2(x, t)) for x in X for t in T) #we are picking a max K value out of all of these. Thus, our N will work for all these values
N=int(np.ceil((M**3*K/(eps*12))**0.5 +1))
print(N)
print(K)

for x in X:
    approx=traps(0,M,N,lambda t:f_gamma(x, t))
    print(f"Approximation of gamma at {x}:",approx)
    print(f"Exact val of gamma at {x}:",gamma(x))
    print(f"Error at {x}:",abs(approx-gamma(x)))
    print("-"*50)