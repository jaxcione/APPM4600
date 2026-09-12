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

x_bar=3
x_vec=np.linspace(0,x_bar,1000)

def bisection(a,b,eps=10**-13):
    if f(a)==0:
        return a 
    if f(b)==0:
        return 0
    if f(a)*f(b)>0:
        return None
    

    d=1/2*(a+b)
    fa=f(a)
    fd=f(d)

    while abs(a-d)/(abs(d))>eps:
        d=1/2*(a+b)
        if f(d)*f(a)==0:
            return d 
        if f(d)*f(a)>0:
            a=d
            fa=fd
        else:
            b=d
            fb=fd
        d=1/2*(a+b)

    return d

print("Your root is:",bisection(0,x_bar))
