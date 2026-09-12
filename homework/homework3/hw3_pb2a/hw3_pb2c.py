import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.special 


alpha=0.138*10**-6
T_s=-15
T_i=20
t=60*3600*24
e=10**-3

m=2*np.sqrt(alpha*t)


def f(x):
    return scipy.special.erf(x/m)-15/35

def f_prime(x):
    return (2/np.sqrt(np.pi)/m)*np.exp(-(x/m)**2)

x_bar=3
x_vec=np.linspace(0,x_bar,1000)

#doing newtons recurssiuvly 
def Netwons(x0,eps=10**-13,z=0):
    if f_prime(x0)==0:
        return "Dividing by zero error"
    
    x=x0-(f(x0)/f_prime(x0))#our recursive statement

    

    if abs(x-z)/abs(x)>eps: #relative error is less than 10**-13
        z=x
        return Netwons(x,eps=10**-13,z=z)
    else: 
        return x

print("Print Starting at x=.01 :",Netwons(.01,10**-13,0)) #staring at .01
print("Print Starting at x=xbar :",Netwons(x_bar,10**-13,0))