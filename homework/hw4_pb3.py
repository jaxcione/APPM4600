import numpy as np
import matplotlib.pyplot as plt

a=3
b=5

def f(x):
  return np.exp(3*x)-27*x**6+27*(x**4)*np.exp(x)-9*(x**2)*np.exp(2*x)

def f_prime(x):
  return 3*np.exp(3*x)-162*x**5+108*(x**3)*np.exp(x)+27*(x**4)*np.exp(x)-18*x*np.exp(2*x)-18*(x**2)*np.exp(2*x)

def f_double_prime(x):
  return 9*np.exp(3*x)-810*x**4+(27*x**4+216*x**3+324*x**2)*np.exp(x)-(36*x**2+72*x+18)*np.exp(2*x)

def h(x):
  return f(x)/f_prime(x)

def h_prime(x):
  return (f_prime(x)**2-f(x)*f_double_prime(x))/(f_prime(x)**2)

#------------------------------------------------------------------------------------------------------------------------------

def Newtons(x0,eps=10**-13,z=0,counter=0):
    if f_prime(x0)==0:
        return "Dividing by zero error"
    
    x=x0-(f(x0)/f_prime(x0))#our recursive statement

    if abs(x-z)/abs(x)>eps: #relative error is less than 10**-13
        z=x
        counter+=1
        return Newtons(x,eps=10**-13,z=z,counter=counter)
    else: 
        return x,f"Iterations:{counter}"

print("Newtons:",Newtons(4,10**-3,z=0,counter=0))

    
    
#modified from problem 1
def modifiedNewtons(x0,eps=10**-13,z=0,counter=0):
    m=3 #multiplicity of f
    if f_prime(x0)==0:
            return "Dividing by zero error"
        
    x=x0-m*(f(x0)/f_prime(x0))#our recursive statement
    
    if abs(x-z)/abs(x)>eps: #relative error is less than 10**-13
            z=x
            counter+=1
            return modifiedNewtons(x,eps=10**-13,z=z,counter=counter)
    else: 
            return x,f"Iterations:{counter}"
    
print("Modified Newtons(m):",modifiedNewtons(4,10**-3,z=0,counter=0))

#using a diff method with h=f/f'
def othermodifiedNewtons(x0,eps=10**-13,z=0,counter=0):
    if f_prime(x0)==0:
                return "Dividing by zero error"
            
    x=x0-(h(x0)/h_prime(x0))#our recursive statement
        
    if abs(x-z)/abs(x)>eps: #relative error is less than 10**-13
                z=x
                counter+=1
                return othermodifiedNewtons(x,eps=10**-13,z=z,counter=counter)
    else: 
                return x,f"Iterations:{counter}"
            
print("Modified Newtons(h(x)):",othermodifiedNewtons(4,10**-3,z=0,counter=0))