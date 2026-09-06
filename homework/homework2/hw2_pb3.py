import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

#part b-----------------------------------------------
def F(x):
    y=math.exp(x)
    return y-1
perterbations=np.arange(-.0000001,.0000001,10**-9)
y=[F(k) for k in perterbations]

#for i, val in enumerate(perterbations):
    #print(f"Perturbation {i}: {val}, F(x): {y[i]}")

#------------------------------------------------------

#part c-----------------------------------------------

x=9.999999995000000E-10
print(f"F({x})={F(x)}")

#part d/e-----------------------------------------------

actual=10**-9


def Taylor_series(y): #taylor series of e when n=2
    return y+y**2/2

def relative_error(z):
    return np.abs(actual-Taylor_series(z))/actual

print(relative_error(x)) #we get 0--> we need two terms in the taylor series to get a better approximation of e^x

sum=0
for k in range(1,10):
    count=0
    error=(10**-16)*actual
    sum+=(x**k/math.factorial(k))
    if np.abs(sum-actual)<error:
        count+=1
        print(f" k={k}")
    if count==1:
        break


#part g-----------------------------------------------
checking=np.expm1(x) #using the built in function to check our answer
print(Taylor_series(x)-checking) #we get 0--> T_2(x) is correct up to 16 digits 


    