import numpy as np
import math 


e=10**-3
b=4
a=1

print(np.log(e/(b-a))/np.log(0.5)) # for problem 5a

#function we are trying to find the root of
def f(x):
    return x**3+x-4

def bisection(a,b,eps):
    counter=0 #storing the num of iterations


    if f(a)==0:
        return a 
    if f(b)==0:
        return b 
    if f(a)*f(b)>0:
        return None
    if abs(a-b)/abs(b)<eps:
        return b
    

    d=.5*(b+a)

    while abs(d-a)/abs(d)>eps:
        counter+=1
        fd=f(d)
        
        if f(d)*f(a)==0:
            return d

        if f(d)*f(a)>0:
            a=d
            fa=fd
        else:
            b=d
         
        d=.5*(b+a)
        fd=f(d)
        

    return (f"Root:{d}",f"Number of Iterations:{counter}")

print(bisection(a,b,e))
