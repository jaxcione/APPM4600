import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as quad

def f_transformed(t):
    if t==0: #obtained by taking the limit of cos(1/t)t
        return 0
    else:
        return np.cos(1/t)*t 


def simpson(a,b,n):

    h=(b-a)/n
    sum_val=h/3*(f_transformed(a)+f_transformed(b))

    
    for k in range(1,int(n/2)):
        sum_val+=(2*h/3)*f_transformed(a+(2*k)*h)

    for j in range(0,int(n/2)):
        sum_val+=(4*h/3)*f_transformed(a+(2*j+1)*h)

    return sum_val

nodes=5
actual_integral=quad.quad(f_transformed,0,1,epsrel=1E-8)
print("Actual integral:", actual_integral[0])
print("Simpson's rule with", nodes, "nodes:", simpson(0,1,nodes-1))