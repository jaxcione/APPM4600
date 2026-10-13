import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize 

def f1(z):
  return z[0]+np.cos(z[0]*z[1]*z[2])-1


def f2(z):
  return (1-z[0])** 0.25 + z[1]+0.05*(z[2]**2)-0.15*z[2] - 1


def f3(z):
  return -(z[0]** 2) -0.1*(z[1] ** 2)+0.01*z[1]+z[2] -1


def F(z):
  return np.array([f1(z),f2(z),f3(z)])

def g(x):
    return f1(x)**2+f2(x)**2+f3(x)**2

def comp_B(m):
    J_m =J(m)
    F_m = F(m)
    grad = J_m.T @ F_m
    return (np.linalg.norm(grad) ** 2) / (np.linalg.norm(J_m @ grad) ** 2)

def J(z):

  df1_d0=1-z[1]*z[2]*np.sin(z[0]*z[1]*z[2])
  df1_d1=-z[0]*z[2]*np.sin(z[0]*z[1]*z[2])
  df1_d2=-z[0]*z[1]*np.sin(z[0]*z[1]*z[2])


  df2_d0 =-.25*(1-z[0])**(-.75)
  df2_d1 =1
  df2_d2 =.1 * z[2]-.15

  df3_d0 =-2*z[0]
  df3_d1 = -.2*z[1]+.01
  df3_d2 = 1

  return np.array( [[df1_d0,df1_d1,df1_d2], [df2_d0,df2_d1,df2_d2],[df3_d0, df3_d1, df3_d2]])

def Newton(x0,eps,Nmax):
    counter=0
    starting=x0
    
    for _ in range(Nmax):
        
        counter=+1
        J_inv=np.linalg.inv(J(x0))
        
        A=F(x0)
        x1=x0-(J_inv@A)
        
        if np.linalg.norm(x1-x0)<eps:
            return x1,counter,f"Converged! Starting point:{starting} "
        
        x0=x1
        
    return x1, "Did not converge"



def steepest_decent(x0,eps,Nmax):
    counter=0
    starting=x0
        
    for _ in range(Nmax):
            Bval=comp_B(x0)
            counter+=1
            
            
            A=F(x0)
            x1=x0-(Bval*(J(x0).T)@A)
            
            if np.linalg.norm(x1-x0)<eps:
                return x1,counter,f"Converged! Starting point:{starting} "
            
            x0=x1
            
    return x1, "Did not converge"

w0=np.array([0,1,0])

#print("Newtons method",Newton(w0,10**-6,1000))
#print("Steepest Decent",steepest_decent(w0,10**-6,1000))

print('Hybrid',Newton(steepest_decent(w0,5*10**-2,1000)[0],10**-6,1000))
