import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import symbols, Eq, solve, Poly

def symbols_func(n,m):
    symbols_a=symbols(f'a0:{n}',seq=True)
    symbols_b=symbols(f'b1:{m}',seq=True)
    symbols_x=symbols('x')

    return np.array(symbols_a), np.array(symbols_b),symbols_x



def pade_coeff_solve(n,m):
    num=0
    denom=1
    a_vec=symbols_func(n,m)[0] #vector of a0,a1,..
    b_vec=symbols_func(n,m)[1] #vector of b1,b2...
    x_symbol=symbols_func(n,m)[2] #making x a symbol s.t we can solve for the coeff 

    for j in range(n):
        num+=a_vec[j]*(x_symbol**j) #creating the numerator

    for i in range(m-1):
        denom+=b_vec[i]*(x_symbol**(i+1)) #creating the denominator

    rhs=denom*taylor(x_symbol,n+m) #multiplying denominator by the taylor(or mclaurin) expansion
    diff=num-rhs #subtracting the lhs and rhs s.t it is set to 0

    eq=[]
    a_and_b=list(a_vec)+list(b_vec) #list of all of our coeff

    Poly_=Poly(diff,x_symbol) #creating a polynomial where x is the main variable. So it groups all terms w respect to x

    #grabbing all the coeff a0,a1,...b1,b2.. etc 
    for s in range(n+m-1):
        coeff=Poly_.nth(s) #crabs the sth coeff which is a function of a and b
        eq.append(Eq(coeff,0)) #sets the eq to 0 

    sol=solve(eq,a_and_b) #solves

    return sol

def taylor(x,r):
    s=0
    for k in range(r):
        s +=(-1)**k/math.factorial(2 * k + 1) * x**(2 * k + 1)
    return s

def pade(n,m,x):
    coeff_lib=pade_coeff_solve(n,m)
    a=[]
    b=[]

    vals=list(coeff_lib.values())

    for t in range(n):
        a.append(vals[t])

    for r in range(n-1,n+m-1):
        b.append(vals[r])

    a=np.array(a)
    b=np.array(b)

    num=0
    denom=1

    for l in range(n):
        num+=a[l]*(x**l) #creating the numerator

    for i in range(m-1):
            denom+=b[i]*(x**(i+1)) #creating the denominator

    return num/denom


X=np.linspace(0,5,1000)
n=4
m=2
Y=pade(n,m,X)
Y2=taylor(X,n+m)

plt.plot(X,Y,label='Pade Approximation',color='purple')
# plt.plot(X,taylor(X,n+m),label='McLaurin Series',color='blue')
plt.legend()
plt.grid()
plt.show()