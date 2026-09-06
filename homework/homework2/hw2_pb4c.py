import numpy as np 
import matplotlib.pyplot as plt
import math 

#obtaining the root of the function using bisection method 

def f(x):
    return 2*x-1-np.sin(x)

def bisection(a,b,eps):
    counter=0
    if f(a)==0:
        return a
    if f(b)==0:
        return b
    if abs(a-b)/abs(b)<eps:
         return b
    if f(a)*f(b)>0:
            return None

    d=1/2*(a+b)
    
    while abs(d-a)/abs(d)>eps:
        counter+=1
        fd=f(d)
        fa=f(a)

        if f(d)*f(a)==0:
            return d 
        if f(a)*f(d)>0:
            a=d
            fa=fd
        else:
             b=d
        d=1/2*(a+b)
        fd=f(d)
    return (f"Root:{d}",f"Number of Iterations:{counter}")
    

print(bisection(0,1,10**-8))
    