import numpy as np 
import matplotlib.pyplot as plt


def g1(x):
  return 3*x[0]**2+4*x[1]**2-1


def g2(x):
  return x[1]**3-8*x[0]**3-1

def G(z):
    return np.array([g1(z),g2(z)])

def iteration(x0,eps,matrix,Nmax):
    counter=0
    for _ in range(Nmax):
        counter+=1
        P=G(x0)
        x1=x0-(matrix@P)
        print(x1)
        
        if np.linalg.norm(x1-x0)>1E10:
            return "Diverged"
        
        if np.linalg.norm(x1-x0)<eps:
            return x1,counter, "Converged!"
        
        x0=x1
        
    return x1,counter, "Did not converge"


v1=np.array([-0.5,0.25])
v2=np.array([-1.5,1.25])
v3=np.array([-3,3])
M=np.array([[.016,-.17],[.52,-.26]])


#print(iteration(v1,10**-4,M,1000))
# print(iteration(v2,10**-4,M,1000))
# print(iteration(v3,10**-4,M,1000))

#----------------------------------------------
#using Newtons method 

def Newton(x0,eps,Nmax):
    counter=0
    starting=x0
    
    for _ in range(Nmax):
        
        counter=+1
        inv_coeff=1/(18*x0[0]*x0[1]**2+192*x0[0]**2*x0[1])
        J_inv=inv_coeff*np.array([[3*x0[1]**2,-8*x0[1]],[24*x0[0]**2,6*x0[0]]])
        
        A=G(x0)
        x1=x0-(J_inv@A)
        
        if np.linalg.norm(x1-x0)<eps:
            return x1,counter,f"Converged! Starting point:{starting} "
        
        x0=x1
        
    return x1, "Did not converge"

print(Newton(v1,10**-4,1000))
print(Newton(v2,10**-4,1000))
print(Newton(v3,10**-4,1000))
        

        
        