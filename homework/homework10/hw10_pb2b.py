import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as quad

def f(x):
    return 1/(1+(x**2))

def traps(a,b,n):
     
    h=(b-a)/n
    sum_val=h/2*(f(a)+f(b))
 

    for k in range(1,n):
        sum_val+=h*f(a+k*h)

    return sum_val
    

def simpson(a,b,n):

    h=(b-a)/n
    sum_val=h/3*(f(a)+f(b))

    
    for k in range(1,int(n/2)):
        sum_val+=(2*h/3)*f(a+(2*k)*h)

    for j in range(0,int(n/2)):
        sum_val+=(4*h/3)*f(a+(2*j+1)*h)

    return sum_val

trap_sci=quad.quad(f,-5,5,epsabs=1E-6,epsrel=0)[0]
trap_sci2=quad.quad(f,-5,5,epsabs=1E-4,epsrel=0)[0]

diff_traps=abs(trap_sci-traps(-5,5,1292))
diff_simpson=abs(trap_sci-simpson(-5,5,108))

diff_traps2=abs(trap_sci2-traps(-5,5,1292))
diff_simpson2=abs(trap_sci2-simpson(-5,5,108))

print(f'|Int-Trap|: {diff_traps}', "Evaluations: 1292")
print(f'|Int-Simpson|: {diff_simpson}', "Evaluations: 108")


print(f'|Int-Trap2|: {diff_traps2}', "Evaluations: 1292")
print(f'|Int-Simpson2|: {diff_simpson2}', "Evaluations: 108")