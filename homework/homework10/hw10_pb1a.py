import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)*np.cos(x)

def traps(a,b,n,tol):
    h=(b-a)/n
    I= -12.070346316389632
    sum_val=h/2*(f(a)+f(b))

    for k in range(1,n):
        sum_val+=h*f(a+k*h)



    if abs(sum_val-I)/abs(I)<tol:
        return sum_val
    else:
        return traps(a,b,2*n,tol)
    

def simpson(a,b,n,tol):
    h=(b-a)/n
    sum_val=h/3*(f(a)+f(b))
    I= -12.070346316389632

    for k in range(1,int(n/2)):
        sum_val+=(2*h/3)*f(a+(2*k)*h)

    for j in range(0,int(n/2)):
        sum_val+=(4*h/3)*f(a+(2*j+1)*h)

   

    
    if abs(sum_val-I)/abs(I)<tol:
        return sum_val
    else:
        return simpson(a,b,2*n,tol)
    
    

print("Simpsons:",simpson(0,np.pi,2,1E-10))
print("Trapezoidal: ",traps(0,np.pi,2,1E-10))